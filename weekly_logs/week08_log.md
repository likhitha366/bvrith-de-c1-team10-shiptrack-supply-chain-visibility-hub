# Week 08 Log — Power BI Dashboard Draft

**Week:** 8  
**Date:** September 2026  
**Team:** 10  
**Project:** ShipTrack — Supply Chain Visibility Hub

---

## 1. Sprint Goal

The goal for Week 08 was to hand the approved Gold outputs to Power BI and create the first working dashboard while preserving the Gold-only reporting boundary.

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Prepared Week 07 Gold outputs for reporting | Team 10 | Done | Gold aggregation work |
| Added Power BI dashboard artifact | Team 10 | Done | `dashboard/Team10-PowerBI-Report.pbix` |
| Updated dashboard folder guidance | Team 10 | Done | `dashboard/README.md` |
| Added Gold sample/export files used for reporting support | Team 10 | Done | `data_sample/gold_exports/` |
| Added dashboard screenshots | Team 10 | Done | `screenshots/` |
| Created dashboard insight documentation | Team 10 | Done | `docs/dashboard_insights.md` |

## 3. Key Decisions

- Continue the **Trusted Silver → Gold → Power BI** flow established in Weeks 06–07.
- Use the approved Gold tables as the reporting layer rather than connecting Power BI directly to raw or Silver detail data.
- Keep the working PBIX under `dashboard/` as the Week 08 dashboard artifact.
- Carry the same dashboard into Week 09 for refinement instead of rebuilding it from scratch.

## 4. Dashboard Inputs

The first Power BI draft (25 September) read the four original Gold tables: `gold_shipment_daily_metrics`, `gold_carrier_metrics`, `gold_route_metrics` and `gold_hub_metrics` (180, 9, 100 and 13 rows). Evidence: `screenshots/week08_gold_connection.png` and `screenshots/week08_powerbi_dashboard.png`.

_Updated 9 October 2026: the Gold layer was rebuilt by 30 September and the report was reconnected to it (`screenshots/week08_power_bi_data.png`). The model in `dashboard/powerbi_1_2_3pages.pbit` now reads the 14 Gold tables below. Fact and summary row counts are the printed output of the last cell of `notebooks/05_gold_aggregations.ipynb`; dimension row counts are from `data_sample/gold_exports/shiptrack_gold_export_manifest.json`._

| Gold table | Kind | Verified rows |
|---|---|---:|
| `gold_fact_shipment` | Fact | 99,857 |
| `gold_fact_shipment_scan` | Fact | 710,666 |
| `gold_fact_shipment_exception` | Fact | 18,330 |
| `gold_shipment_delay_summary` | Summary | 52,381 |
| `gold_carrier_performance_summary` | Summary | 4,936 |
| `gold_route_reliability_summary` | Summary | 17,930 |
| `gold_hub_throughput_summary` | Summary | 9,445 |
| `gold_shipment_status_exception_summary` | Summary | 47 |
| `gold_dim_date` | Dimension | 365 |
| `gold_dim_hub` | Dimension | 14 |
| `gold_dim_carrier` | Dimension | 10 |
| `gold_dim_route` | Dimension | 103 |
| `gold_dim_service_level` | Dimension | 3 |
| `gold_dim_status` | Dimension | 6 |

## 5. Evidence Added to GitHub

- `dashboard/Team10-PowerBI-Report.pbix`
- `dashboard/README.md`
- `data_sample/gold_exports/`
- dashboard screenshots under `screenshots/`
- `docs/dashboard_insights.md`

## 6. AI Transparency Note

| Question | Response |
|---|---|
| **Where AI helped** | AI assisted with repository review, documentation structure and checking that the dashboard documentation followed the Week 08 requirements. |
| **What we changed after AI suggestion** | Documentation was adapted to the actual ShipTrack Gold tables, PBIX filename and repository evidence. |
| **What we verified manually** | The repository contains the PBIX artifact, Gold export files, dashboard documentation and screenshots. |
| **What we can explain without AI** | The team can explain the Gold-to-Power-BI flow, Gold table purposes and the dashboard reporting scope. |

## 7. Blockers / Risks

- PBIX internals are binary and cannot be reviewed as ordinary Markdown/source content through GitHub.
- Final KPI reconciliation must use the same filter state as the Power BI visual and the owning Gold table.
- Week 09 refinement should not introduce unsafe relationships or bypass the Gold-only source rule.

## 8. Next Week Preparation

- Refine the existing Power BI dashboard.
- Check visual hierarchy, labels, formatting and filter behaviour.
- Reconcile important dashboard values to their owning Gold tables.
- Document evidence-backed observations and limitations in `docs/dashboard_insights.md`.
