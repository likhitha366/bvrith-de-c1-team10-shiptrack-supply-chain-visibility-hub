# Week 10 Log — Streaming Simulation and Live Scan Events

**Week:** 10
**Date range:** 29 September – 5 October 2026
**Team:** Team 10
**Project:** ShipTrack: Supply Chain Visibility Hub

---

## 1. Sprint Goal

Show ShipTrack scan events arriving over time using two patterns: incremental JSON file ingestion with Auto Loader (five controlled drops from the approved data pack) and live scan events processed by a continuous SQL pipeline. Route replayed, late, orphan, malformed and schema-drift events with evidence, and prove that a run with no new file adds nothing.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Copied the five approved drops to `data_sample/streaming/` and checked line counts against `source_manifest.csv` (12 / 14 / 14 / 15 / 15) | B. Likhitha | Done | `data_sample/streaming/` |
| Wrote the ShipTrack event contract | G. Shivani | Done | `streaming/kafka_event_schema.json` |
| Wrote the streaming design | G. Shivani | Done | `streaming/structured_streaming_design.md` |
| Built the Week-10 notebook (Auto Loader, stream DQ, Gold fact, live producer) | R. Meenakshi Reddy | Done | `notebooks/07_streaming_simulation.ipynb` |
| Ran the five drops one at a time in Databricks and reconciled per file | B. Likhitha | In progress — Databricks run and screenshots pending | `week10_01` – `week10_04` |
| Ran stream DQ, reconciliation and no-new-file rerun | R. Meenakshi Reddy | In progress — Databricks run and screenshots pending | `week10_05` – `week10_09` |
| Ran the continuous pipeline, producer, count growth and stop/restart | G. Shivani | In progress — Databricks run and screenshots pending | `week10_10` – `week10_13` |

---

## 3. Key Decisions

- Two examples are used because file arrival and live event arrival show different sides of data in motion.
- Auto Loader reads each file line by line so that Bronze keeps every physical line, including the malformed one. Bronze does not deduplicate or repair.
- The exact playbook table names are used: `bronze_scan_event_stream`, `silver_candidate_scan_events`, `trusted_silver_scan_events`, `quarantine_scan_events`, `gold_fact_scan_event`.
- `event_id` is the deduplication key: the first arrival is trusted and the replay is quarantined with its reason. For a sequence conflict both rows fail, because there is no approved winner.
- The 24-hour watermark is calculated in SQL and stored as `watermark_status` and `is_late`, so a late event is visible instead of being silently dropped.
- Trigger `availableNow` is used because Databricks Free Edition runs on serverless compute.
- Kafka is design-only. No broker or topic was created.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| All five drop files have the same name (`scan_event.json`) | They cannot be uploaded into one folder | Solved in the notebook: `find_drop()` accepts the pack folder layout or files renamed to the drop name |
| Reference tables for hubs, carriers and routes may not exist with the `trusted_silver_` prefix | Stream reference checks would use Silver instead of Trusted | Notebook section 10 prints which table is used; mentor to confirm if a Silver fallback is acceptable |
| The continuous pipeline must be created in the Databricks UI | If it is set to Triggered, live Bronze will not keep updating | Use Serverless ON and Pipeline mode Continuous (notebook section 18) |

---

## 5. Evidence Added to GitHub

- `notebooks/07_streaming_simulation.ipynb` — Week-10 notebook at the exact starter path.
- `streaming/structured_streaming_design.md` — design, controls, targets and run behaviour.
- `streaming/kafka_event_schema.json` — event contract only (Kafka not installed).
- `data_sample/streaming/` — the five approved drops, unchanged.
- `weekly_logs/week10_log.md` — this log.
- `screenshots/week10_*` — added after the Databricks run (names in notebook section 22).

### Executed results

Recorded from the team's own Databricks run of the notebook. Source-pack line counts are not results.

| Check | Notebook cell | Result |
|---|---|---|
| Bronze physical rows, all files | 9.1 | pending Databricks run |
| Candidate / Trusted / Quarantine and variance | 15.1 | pending Databricks run |
| Failed events per rule | 15.2 | pending Databricks run |
| Outside-watermark events | 15.4 | pending Databricks run |
| No-new-file rerun differences | 16.3 | pending Databricks run |
| Live count before / after producer stop | 20.2, 21 | pending Databricks run |

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI drafted the Week-10 notebook, the streaming design document and the event contract from the approved P10 playbook, the cohort Week-10 guide and the five official drop files, and explained Auto Loader, checkpoints and watermark behaviour. |
| What we changed after AI suggestion | Before running we confirm the catalog, schema and volume path for our workspace and the reference tables printed in notebook section 10. Any cell changed during the Databricks run is listed in this row. |
| What we verified manually | Source line counts against `source_manifest.csv`; in the Databricks run we check per-file Bronze counts, the replayed `event_id`, the quarantine reasons, the reconciliation, the no-new-file rerun and the live count growth before saving screenshots. |
| What we can explain without AI | Producer → landing → Auto Loader → checkpoint → Bronze → Candidate → Trusted / Quarantine → Gold; why a replayed `event_id` is not a checkpoint problem; how the 24-hour watermark is calculated; why the count stops when the producer stops. |

---

## 7. Next Week Preparation

- Keep the Week-10 implementation stable; add no further streaming features.
- Carry the stream tables and evidence into the Week-11 pipeline walkthrough and run order.
- Update `README.md`, `docs/pipeline_walkthrough.md` and `docs/references.md` in Week 11.
