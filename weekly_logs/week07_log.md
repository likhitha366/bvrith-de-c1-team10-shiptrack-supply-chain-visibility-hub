# Week 07 Log — Gold Layer Development

**Week:** 7  
**Date range:** 8 September – 14 September 2026  
**Team:** 10  
**Project:** ShipTrack — Supply Chain Visibility Hub

---

## 1. Sprint Goal

The goal for Week 07 was to develop and validate the Gold layer using the Trusted shipment data produced by the Week 06 data-quality process. The Gold layer converts trusted shipment records into business-ready aggregates for reporting and analytics.

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Built the shipment, scan and exception Gold facts | Team 10 | Done | Gold aggregation notebook |
| Built the delay, carrier, route and hub Gold summaries | Team 10 | Done | Gold aggregation notebook |
| Built the open-status and exception snapshot summary | Team 10 | Done | Gold aggregation notebook |
| Used `trusted_shipments`, `trusted_scan_events` and `trusted_exceptions` as the only Gold sources | Team 10 | Done | Gold SQL / notebook |
| Validated Gold outputs and aggregation grains | Team 10 | Done | Gold validation output |
| Updated `docs/gold_metrics_definition.md` | Team 10 | Done | GitHub |

## 3. Implemented Gold Tables

_Updated 9 October 2026: the first Week 7 build (25 September) produced four Gold tables: `gold_shipment_daily_metrics` (180 rows), `gold_carrier_metrics` (9), `gold_route_metrics` (100) and `gold_hub_metrics` (13). The Gold layer was rebuilt by 30 September as the facts and summaries below, which are what `notebooks/05_gold_aggregations.ipynb` builds now. Row counts are the printed output of its last cell._

| Gold Table | Grain | Verified Rows |
|---|---|---:|
| `gold_fact_shipment` | One row per trusted shipment | 99,857 |
| `gold_fact_shipment_scan` | One row per trusted historical scan | 710,666 |
| `gold_fact_shipment_exception` | One row per exception occurrence | 18,330 |
| `gold_shipment_delay_summary` | Delivery date × route × carrier × service level × delay band | 52,381 |
| `gold_carrier_performance_summary` | Delivery date × carrier × service level | 4,936 |
| `gold_route_reliability_summary` | Delivery date × route × service level | 17,930 |
| `gold_hub_throughput_summary` | Event date × time band × hub | 9,445 |
| `gold_shipment_status_exception_summary` | Snapshot date × status × ageing band × exception type | 47 |

The Gold layer reads only the Week 06 Trusted tables (`trusted_shipments`, `trusted_scan_events`, `trusted_exceptions`), preserving the Trusted-versus-Quarantine separation.

## 4. Key Decisions

- Gold reporting datasets are built from Trusted shipment data.
- Each Gold table keeps its own reporting grain.
- The three Gold facts and five Gold summaries are used as downstream reporting sources rather than rebuilding upstream transformations in Power BI.
- The Gold metric definitions document the intended business use of each table.

## 5. Validation

The completed Gold outputs were checked for successful creation, expected aggregation grain and current row counts:

- `gold_fact_shipment`: 99,857
- `gold_fact_shipment_scan`: 710,666
- `gold_fact_shipment_exception`: 18,330
- `gold_shipment_delay_summary`: 52,381
- `gold_carrier_performance_summary`: 4,936
- `gold_route_reliability_summary`: 17,930
- `gold_hub_throughput_summary`: 9,445
- `gold_shipment_status_exception_summary`: 47

These counts represent the executed Week 07 dataset and can change if the Trusted input data changes.

## 6. Data Flow

```text
Raw Data
   ↓
Bronze
   ↓
Silver
   ↓
Week 06 DQ Evaluation
   ↓
Trusted Silver
   ↓
Gold
   ├── Facts: shipment, shipment scan, shipment exception
   └── Summaries: delay, carrier performance, route reliability, hub throughput, status and exception
   ↓
Power BI / Reporting
```

## 7. Blockers / Risks

- Gold metrics depend on the current Trusted Silver dataset.
- Any upstream DQ or schema change may affect downstream Gold outputs.
- Gold metric definitions must remain aligned with the implemented notebook columns and SQL logic.

## 8. AI Transparency Note

| Question | Response |
|---|---|
| **Where AI helped** | AI assisted with aggregation-logic review and documentation structure. |
| **What we changed after AI suggestion** | The implementation and documentation were aligned with the actual ShipTrack schema, Trusted shipment source and project requirements. |
| **What we verified manually** | Gold sources, aggregation grains, output row counts and metric definitions were checked against the implemented work. |
| **What we can explain without AI** | The team can explain the Trusted-to-Gold flow, aggregation grains, business metrics and validation process. |

## 9. Next Week Preparation

- Prepare the approved Gold outputs for Power BI.
- Create the first Gold-only dashboard/reporting layer.
- Preserve the Trusted → Gold data flow.
- Capture dashboard and Gold hand-off evidence.
