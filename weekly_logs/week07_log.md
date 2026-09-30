# Week 07 Log — Gold Layer Development

**Week:** 7  
**Team:** 10  
**Project:** ShipTrack — Supply Chain Visibility Hub

---

## 1. Sprint Goal

The goal for Week 07 was to develop and validate the Gold layer using the Trusted shipment data produced by the Week 06 data-quality process. The Gold layer converts trusted shipment records into business-ready aggregates for reporting and analytics.

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Developed daily shipment Gold metrics | Team 10 | Done | Gold aggregation notebook |
| Developed carrier-level Gold metrics | Team 10 | Done | Gold aggregation notebook |
| Developed route-level Gold metrics | Team 10 | Done | Gold aggregation notebook |
| Developed hub-level Gold metrics | Team 10 | Done | Gold aggregation notebook |
| Used `trusted_shipments` as the Gold source | Team 10 | Done | Gold SQL / notebook |
| Validated Gold outputs and aggregation grains | Team 10 | Done | Gold validation output |
| Updated `docs/gold_metrics_definition.md` | Team 10 | Done | GitHub |

## 3. Implemented Gold Tables

| Gold Table | Grain | Verified Rows |
|---|---|---:|
| `gold_shipment_daily_metrics` | One row per booking date | 180 |
| `gold_carrier_metrics` | One row per carrier | 9 |
| `gold_route_metrics` | One row per route | 100 |
| `gold_hub_metrics` | One row per hub | 13 |

The Gold layer uses `trusted_shipments` as the shipment source, preserving the Week 06 Trusted-versus-Quarantine separation.

## 4. Key Decisions

- Gold reporting datasets are built from Trusted shipment data.
- Each Gold table keeps its own reporting grain.
- The four Gold tables are used as downstream reporting sources rather than rebuilding upstream transformations in Power BI.
- The Gold metric definitions document the intended business use of each table.

## 5. Validation

The completed Gold outputs were checked for successful creation, expected aggregation grain and current row counts:

- `gold_shipment_daily_metrics`: 180
- `gold_carrier_metrics`: 9
- `gold_route_metrics`: 100
- `gold_hub_metrics`: 13

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
Gold Aggregations
   ├── Daily Shipment Metrics
   ├── Carrier Metrics
   ├── Route Metrics
   └── Hub Metrics
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
