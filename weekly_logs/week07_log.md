# Week 07 Log — Gold Layer Development

**Week:** 7  
**Team:** 10  
**Project:** ShipTrack  

---

## 1. Sprint Goal

The goal for Week 07 was to develop and validate the **Gold layer** of the ShipTrack data pipeline using the Trusted Silver shipment data produced by the Week 06 data-quality framework.

The Gold layer converts trusted shipment records into business-ready aggregated datasets for reporting and analytics.

---

## 2. Work Completed

| Task | Status | Evidence |
|---|---|---|
| Developed daily shipment Gold metrics | Done | Gold aggregation notebook |
| Developed carrier-level Gold metrics | Done | Gold aggregation notebook |
| Developed route-level Gold metrics | Done | Gold aggregation notebook |
| Developed hub-level Gold metrics | Done | Gold aggregation notebook |
| Configured Gold transformations to use `trusted_shipments` | Done | Gold SQL / notebook |
| Validated Gold outputs and row counts | Done | Gold validation output |
| Documented Gold metrics and data flow | Done | `docs/gold_metrics_definition.md` |
| Updated project documentation in GitHub | Done | GitHub repository |

---

## 3. Implemented Gold Tables

| Gold Table | Grain | Verified Rows |
|---|---|---:|
| `gold_shipment_daily_metrics` | One row per booking date | 180 |
| `gold_carrier_metrics` | One row per carrier | 9 |
| `gold_route_metrics` | One row per route | 100 |
| `gold_hub_metrics` | One row per hub | 13 |

The Gold layer uses `trusted_shipments` as its shipment source. This preserves the Week 06 isolation between trusted and quarantined records.

---

## 4. Key Metrics

The Gold layer supports business metrics including:

- Shipment volume
- Delivered shipments
- Delayed deliveries
- Delivery rate
- On-time delivery rate
- Average delivery hours
- Total freight
- Hub flow counts

The exact SQL expressions and output columns are defined by the Gold aggregation notebook.

---

## 5. Validation

The completed Gold outputs were checked for successful table creation and expected aggregation grain.

Current verified row counts:

- `gold_shipment_daily_metrics`: 180
- `gold_carrier_metrics`: 9
- `gold_route_metrics`: 100
- `gold_hub_metrics`: 13

The Gold layer is intended to be the downstream source for Week 08 dashboard/reporting work.

---

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
Dashboard / Reporting
```

---

## 7. Blockers / Risks

- Gold metrics depend on the current Trusted Silver dataset and may change if the upstream DQ results change.
- Dashboard development is a downstream Week 08 activity.
- Gold metric definitions should remain synchronized with the implemented notebook columns and SQL logic.

---

## 8. AI Transparency Note

| Question | Response |
|---|---|
| **Where AI helped** | AI assisted with drafting Gold aggregation logic and documentation structure. |
| **What we changed after AI suggestion** | The implementation was aligned with the actual ShipTrack Silver schema, Trusted shipment data, and project requirements. |
| **What we verified manually** | Gold table sources, aggregation outputs, row counts, and metric definitions were checked against the implemented notebook and Databricks results. |
| **What we can explain without AI** | We can explain the Silver-to-Trusted-to-Gold flow, aggregation grains, business metrics, and validation process. |

---

## 9. Next Week Preparation

- Connect the Gold outputs to the reporting/dashboard layer.
- Build required Week 08 visuals using Gold tables.
- Preserve the Trusted → Gold data flow.
- Capture final Gold validation evidence for project submission.
