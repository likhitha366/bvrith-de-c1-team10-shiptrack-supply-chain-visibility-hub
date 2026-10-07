# Gold Metrics Definition

**Week:** 7 | **Team:** 10 | **Project:** ShipTrack: Supply Chain Visibility Hub
**Implementation:** `notebooks/05_gold_aggregations.ipynb` (executed) | **Source rule:** Gold reads Trusted Silver only

---

## 1. Business questions

| # | Question | KPI family |
|---|---|---|
| 1 | How many shipments did we handle and how many were delivered? | Volume |
| 2 | How reliably do we deliver against the promise? | On-time delivery |
| 3 | When we are late, how late? | Delivery delay |
| 4 | How long does a shipment take end to end? | Transit time |
| 5 | How often does a shipment hit an exception? | Exceptions |
| 6 | How often is the first delivery attempt successful? | First-attempt success |
| 7 | How long do shipments wait at a hub? | Hub dwell |
| 8 | What is still open, and how old is it? | Backlog and ageing |

## 2. Gold table catalog

Trusted inputs resolved in the executed notebook: `trusted_shipments`, `trusted_scan_events`, `trusted_exceptions`. Silver Candidate and Quarantine are not read.

### Facts

| Gold table | Grain (one row per) | Key | Rows (executed Week-7 run) |
|---|---|---|---:|
| `gold_fact_shipment` | trusted shipment | `shipment_id` | 99,857 |
| `gold_fact_shipment_scan` | trusted historical scan | `scan_id` | 710,666 |
| `gold_fact_shipment_exception` | trusted exception occurrence | `exception_id` | 18,330 |
| `gold_fact_scan_event` | trusted streaming event | `event_id` | built in Week 10 (`notebooks/07_streaming_simulation.ipynb`) |

### Summaries

| Gold table | Grain (one row per) | Built from | Rows (executed Week-7 run) |
|---|---|---|---:|
| `gold_shipment_delay_summary` | `delivery_date`, `route_id`, `carrier_id`, `service_level`, `delay_band` | `gold_fact_shipment` (delivered only) | 52,381 |
| `gold_carrier_performance_summary` | `delivery_date`, `carrier_id`, `service_level` | `gold_fact_shipment` | 4,936 |
| `gold_route_reliability_summary` | `delivery_date`, `route_id`, `service_level` | `gold_fact_shipment` | 17,930 |
| `gold_hub_throughput_summary` | `event_date`, `time_band`, `hub_id` | `gold_fact_shipment_scan` | 9,445 |
| `gold_shipment_status_exception_summary` | `snapshot_date`, `latest_status`, `ageing_band`, `exception_type` | `gold_fact_shipment` + exception roll-up | 47 |

Row counts are the printed output of the last cell of the executed notebook. They change if Trusted Silver changes.

Conformed dimensions used by Power BI (`gold_dim_date`, `gold_dim_hub`, `gold_dim_carrier`, `gold_dim_route`, `gold_dim_service_level`, `gold_dim_status`) are registered in `notebooks/06_powerbi_export.ipynb`.

## 3. Derived fields on `gold_fact_shipment`

Calculated once at shipment grain so that scans and exceptions can never multiply shipment measures.

| Field | Formula |
|---|---|
| `delivered_flag` | 1 when `delivery_outcome = 'DELIVERED'`, else 0 |
| `delivery_delay_minutes` | for delivered shipments with both timestamps: `GREATEST((actual_delivery_ts − promised_delivery_ts) in minutes, 0)`; otherwise NULL |
| `transit_hours` | for delivered shipments: `(actual_delivery_ts − pickup_ts)` in hours; otherwise NULL |
| `on_time_flag` | 1 when delivered and `actual_delivery_ts <= promised_delivery_ts`, else 0 |
| `first_attempt_success_flag` | 1 when delivered and `attempt_count = 1`, else 0 |
| `booking_date`, `delivery_date` | `CAST(booking_ts AS DATE)`, `CAST(actual_delivery_ts AS DATE)` |

Duplicate protection: if a `shipment_id` appears more than once in Trusted, the row with the lowest `source_record_id` is kept (`ROW_NUMBER() ... rn = 1`).

## 4. KPI contracts

All shipment KPIs count **distinct `shipment_id`** on `gold_fact_shipment`.

| KPI | Formula | Eligible rows | Zero-denominator result |
|---|---|---|---|
| Total Shipments | `COUNT(DISTINCT shipment_id)` | all trusted shipments | 0 |
| Delivered Shipments | `COUNT(DISTINCT shipment_id)` where `delivered_flag = 1` | all trusted shipments | 0 |
| On-Time Delivery Rate % | on-time delivered ÷ delivered, × 100 | delivered with a non-null `promised_delivery_ts` | NULL |
| Average Delivery Delay (late only) | `AVG(delivery_delay_minutes)` where `delivery_delay_minutes > 0` | delivered and late | NULL |
| Average End-to-End Transit Hours | `AVG(transit_hours)` | delivered with `transit_hours` not null | NULL |
| Exception Rate % | distinct shipments in `gold_fact_shipment_exception` ÷ Total Shipments, × 100 | all trusted shipments | 0 |
| First-Attempt Delivery Success Rate % | delivered with `attempt_count = 1` ÷ delivered with `attempt_count` not null, × 100 | delivered | NULL |
| Hub Average Dwell Minutes | `AVG` of minutes between an `AT_HUB` scan and the next scan at the same hub with status `IN_TRANSIT` or `OUT_FOR_DELIVERY` | hub visits with a following departure scan | NULL |

### Bands

| Band | Values |
|---|---|
| `delay_band` | `ON_TIME` (0 min), `LATE_1_60_MIN`, `LATE_61_240_MIN`, `LATE_240_PLUS_MIN` |
| `time_band` (hub arrival hour) | `00_06`, `06_12`, `12_18`, `18_24` |
| `ageing_band` (days since booking for non-delivered shipments) | `0_2_DAYS`, `3_7_DAYS`, `8_14_DAYS`, `15_PLUS_DAYS` |

## 5. Grain warning

Scans and exceptions are one-to-many children of a shipment. Shipment weight, freight and delivery measures are never summed at scan or exception grain. Exception rate returns to distinct `shipment_id` before it is used as a shipment KPI.

## 6. Validations executed in the notebook

| Check | Notebook section | Pass condition |
|---|---|---|
| Fact key uniqueness (`shipment_id`, `scan_id`, `exception_id`) | 8 | 0 duplicate keys |
| Measure validity (negative freight, weight, package count, delay; invalid flags) | 8 | 0 failures |
| Summary grain uniqueness (five summaries) | 8 | `duplicate_grain_rows = 0` |
| KPI reconciliation by `booking_date` back to `gold_fact_shipment` | 9 | all differences 0 |
| Manual spot checks, including an edge case | 10 | records readable and explainable |
| Controlled rerun (`CREATE OR REPLACE TABLE ... USING DELTA`) | 11 | row counts and distinct keys unchanged |

## 7. Known caveats

- `gold_fact_shipment_exception` holds 18,330 rows; 19 `shipment_id` values in it have no row in `gold_fact_shipment` (shipments quarantined in Week 6). `notebooks/06_powerbi_export.ipynb` reports this and filters them from the export (18,306 rows exported).
- In `gold_shipment_delay_summary`, a delivered shipment with no valid promise has a NULL delay and falls into `LATE_240_PLUS_MIN`. The export notebook checks this case (section 3c).
- `gold_shipment_status_exception_summary` is a snapshot: `snapshot_date` and ageing depend on the run date.

## 8. Downstream use

Power BI reads these Gold tables only. Page-to-table mapping and reconciliation are in `dashboard/README.md`; insights are in `docs/dashboard_insights.md`.
