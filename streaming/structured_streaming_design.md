# Structured Streaming Design — ShipTrack

**Week:** 10 | **Team:** 10 | **Project:** P10 ShipTrack — Supply Chain Visibility Hub
**Implementation:** `notebooks/07_streaming_simulation.ipynb` | **Event contract:** `streaming/kafka_event_schema.json`

---

## 1. Objective

Show ShipTrack scan events arriving over time in two ways: incremental file ingestion with Auto Loader (five controlled drops) and live scan events processed by a continuous SQL pipeline. Prove that only new input is processed and that bad events are routed with evidence.

## 2. Event source

| Example | Source | Location |
|---|---|---|
| A — file drops | five newline-delimited JSON files from the approved P10 data pack | repo: `data_sample/streaming/drop_0X_*/scan_event.json`; Databricks: `/Volumes/workspace/default/shiptrack_stream/week10_source/` |
| C — live events | Delta source table `shiptrack_live_scan_events` | `workspace.default` |

Source-pack line counts (from `source_manifest.csv`): 12, 14, 14, 15, 15 = 70 physical lines.

## 3. Producer

| Example | Producer |
|---|---|
| A | `land(<drop>)` copies **one** drop at a time from `week10_source/` to `week10_landing/` |
| C | `produce(first, last)` inserts one live scan event every 3 seconds; 30 events = 6 shipments × `PICKED_UP → IN_TRANSIT → AT_HUB → OUT_FOR_DELIVERY → DELIVERED` |

## 4. Event contract

21 declared fields, `schema_version` must be `1.0`. Required: `source_record_id`, `event_id`, `shipment_id`, `event_sequence_no`, `event_type`, `shipment_status`, `event_time`, `hub_id`, `carrier_id`, `route_id`. Deduplication key: `event_id`. Ordering key inside a shipment: `event_sequence_no`. Full definition: `kafka_event_schema.json`.

## 5. Processing

| Step | Method | Notes |
|---|---|---|
| File arrival → Bronze | Auto Loader (`cloudFiles`, format `text`), explicit schema applied with `from_json`, trigger `availableNow` | each physical line is kept in `raw_line`, so malformed lines are not lost |
| Checkpoint | `/Volumes/workspace/default/shiptrack_stream/week10_checkpoint/bronze_scan_event_stream` | separate from the landing folder and from the output table |
| Bronze → Candidate → Trusted / Quarantine → Gold | Spark SQL rebuild from streaming Bronze (`CREATE OR REPLACE TABLE`) | rerun after new drops; same Bronze gives the same split |
| Live events → Bronze | continuous SQL pipeline: `CREATE OR REFRESH STREAMING TABLE ... FROM STREAM(shiptrack_live_scan_events)` | pipeline stays running; it is not re-run per event |

### Controls

| Control | Decision |
|---|---|
| Schema | explicit; undeclared fields are listed in `_unexpected_fields`; nothing is inferred |
| Deduplication | `event_id`; the first arrival is trusted, a replay goes to Quarantine with the reason kept |
| Sequence conflict | two `event_id` values on one `(shipment_id, event_sequence_no)` → both rows fail (no arbitrary winner) |
| Watermark | 24 hours on `event_time`. Watermark = latest `event_time` seen in earlier arrivals − 24 h. `watermark_status` and `is_late` are stored on every event |
| Late events | inside the watermark → trusted with `is_late = true`; outside → Quarantine |
| Malformed / drift | raw line, source file and undeclared fields are retained under `DQ-EVT-001` |
| References | shipment, hub, carrier, route and route lane are checked against the Week-6 trusted references |

The watermark is calculated in SQL instead of with a stateful stream operator. Reason: a stateful watermark drops late rows silently, while the project rule is that no failed record is silently deleted.

## 6. Targets

| Table | Grain | Purpose |
|---|---|---|
| `bronze_scan_event_stream` | one physical line | append-only streaming Bronze with lineage |
| `silver_candidate_scan_events` | one Bronze line (`source_record_id`) | typed and standardised, nothing filtered |
| `stream_scan_event_dq_results` | one Candidate row | every rule flag, `failed_rule_list`, reason, severity |
| `trusted_silver_scan_events` | one passed event | Gold-eligible events |
| `quarantine_scan_event_stream` | one failed event | all failed rules, raw payload, lineage, `rework_status` |
| `gold_fact_scan_event` | one trusted streaming event (`event_id`) | live feed for reporting |
| `bronze_shiptrack_live_scan_events` | one live event | output of the continuous pipeline |

Naming note: the Week-6 batch scan tables are already called `trusted_scan_events` and `quarantine_scan_events`. The stream quarantine table is therefore named `quarantine_scan_event_stream` so that the Week-10 notebook can never overwrite Week-6 results.

Rules applied to streamed events: `DQ-EVT-001`, `DQ-REF-001`, `DQ-SCN-001`, `DQ-TIM-001`, `DQ-DEL-001`.

## 7. Run behaviour

- A new file in landing is processed once. A run with no new file appends nothing to Bronze.
- Rebuilding Candidate / Trusted / Quarantine / Gold from unchanged Bronze gives unchanged counts.
- Live Bronze grows only while the producer is running.

## 8. Near-real-time metric

| Metric | Formula | Use |
|---|---|---|
| Trusted scan events by hub and status | `COUNT(*)` from `gold_fact_scan_event` grouped by `hub_id`, `shipment_status` | where shipments are right now |
| Late events | `SUM(is_late)` in the same query | how much of the feed arrives out of order |
| Live events by hub and status | `COUNT(*)` from `bronze_shiptrack_live_scan_events` | changes while the producer runs |

## 9. Evidence

Per-file reconciliation, checkpoint file state (`cloud_files_state`), no-new-file proof, Candidate = Trusted + Quarantine reconciliation, quarantine reasons, watermark status, live count growth and stop/restart. Screenshot names are listed in section 22 of the notebook. Executed counts are recorded in `weekly_logs/week10_log.md`, not here.

## 10. Recovery

Use the reset cell (section 23) only before a completely fresh run: it drops the Week-10 stream tables and clears landing and checkpoint. Source drops are never changed. A quarantined event is not edited by hand: the upstream drop is corrected, landed again as a new file, and Part B is rebuilt.

## 11. Boundary and limitations

- No Kafka broker, topic, partition or consumer configuration. Kafka is design-only.
- No Gold KPI redesign and no Power BI change in Week 10.
- The drops are synthetic continuations of historical shipments, so lifecycle validity uses the producer marker `INVALID_AFTER_DELIVERY` and the delivered-at-destination check, not a comparison with the batch terminal status.
- `availableNow` is used because Databricks Free Edition runs on serverless compute. Live events use `LIVE-` IDs and are not loaded into Gold.
