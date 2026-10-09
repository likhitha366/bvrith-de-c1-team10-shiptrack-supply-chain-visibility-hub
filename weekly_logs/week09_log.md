# Week 09 Log — Dashboard Refinement and Insight Communication

**Week:** 9  
**Date range:** 22 September – 28 September 2026  
**Team:** 10  
**Project:** ShipTrack — Supply Chain Visibility Hub

---

## 1. Sprint Goal

The goal for Week 09 was to carry the Week 08 Gold-only Power BI dashboard forward, refine its presentation and usability, and document evidence-backed dashboard observations without changing the underlying Gold business meaning.

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Carried the Week 08 report forward into the three-page version | Team 10 | Done | `dashboard/powerbi_1_2_3pages.pbit` |
| Kept Gold tables as the reporting sources | Team 10 | Done | `dashboard/README.md`, Gold documentation |
| Reviewed dashboard structure and business-question mapping | Team 10 | Done | Dashboard documentation |
| Updated dashboard insight documentation | Team 10 | Done | `docs/dashboard_insights.md` |
| Updated dashboard README with Week 09 refinement rules | Team 10 | Done | `dashboard/README.md` |
| Updated Week 07 Gold definitions for downstream traceability | Team 10 | Done | `docs/gold_metrics_definition.md` |
| Added screenshots of the three refined pages | Team 10 | Done | `screenshots/week09_powerbi_overview.png`, `screenshots/week09_powerbi_performance.png`, `screenshots/week09_powerbi_exceptions_live.png` |
| Added a filtered-reconciliation screenshot | Team 10 | Not yet available | `screenshots/` |

## 3. Key Decisions

- Week 09 uses the existing Week 08 dashboard as the starting point rather than creating a new dashboard from scratch.
- The approved Gold facts, summaries and dimensions remain the only reporting sources.
- Dashboard insights describe observable data patterns and do not claim causes that are not supported by the Gold data.
- Different Gold grains are kept conceptually separate; no unsafe relationship is introduced merely to force unrelated tables to share filters.

## 4. Dashboard / Gold Mapping

_Updated 9 October 2026: an earlier version of this log listed the four original Gold tables (`gold_shipment_daily_metrics`, `gold_carrier_metrics`, `gold_route_metrics`, `gold_hub_metrics`). The refined dashboard does not use them; it reads the rebuilt Gold layer below. Row counts are the printed output of the last cell of `notebooks/05_gold_aggregations.ipynb`._

| Analysis | Owning Gold Table | Current Verified Rows |
|---|---|---:|
| Shipment volume, delivery, on-time rate and transit | `gold_fact_shipment` | 99,857 |
| Scan milestone timeline | `gold_fact_shipment_scan` | 710,666 |
| Exception counts and severity | `gold_fact_shipment_exception` | 18,330 |
| Delay bands | `gold_shipment_delay_summary` | 52,381 |
| Carrier comparison | `gold_carrier_performance_summary` | 4,936 |
| Route reliability | `gold_route_reliability_summary` | 17,930 |
| Hub throughput and dwell | `gold_hub_throughput_summary` | 9,445 |
| Open backlog and ageing | `gold_shipment_status_exception_summary` | 47 |
| Slicers and labels | `gold_dim_date`, `gold_dim_hub`, `gold_dim_carrier`, `gold_dim_route`, `gold_dim_service_level`, `gold_dim_status` | 365 / 14 / 10 / 103 / 3 / 6 |

The row counts are the verified Gold outputs documented from Week 07 and the Week 08 export manifest, and are not claimed as new Week 09 measurements.

## 5. Evidence Added to GitHub

- `docs/dashboard_insights.md` — Week 09 insight and limitation documentation.
- `dashboard/README.md` — final source/model/refinement guidance.
- `docs/gold_metrics_definition.md` — Gold definitions carried through the reporting stage.
- `weekly_logs/week07_log.md`
- `weekly_logs/week08_log.md`
- `weekly_logs/week09_log.md`

The three refined pages are in `screenshots/week09_powerbi_*.png`. They were first committed on 30 September under `week08_` names and renamed on 9 October 2026; the images are unchanged. The Overview capture has slicers applied (carrier, region, route, service level). A filtered-reconciliation screenshot has not been captured and is not marked as present.

## 6. AI Transparency Note

| Question | Response |
|---|---|
| **Where AI helped** | AI assisted with checking the repository against the Week 09 guide and structuring the Markdown documentation. |
| **What we changed after AI suggestion** | The documentation was adapted to the actual ShipTrack Gold table names, PBIX filename and verified repository evidence. |
| **What we verified manually** | Gold table names, verified row counts, PBIX path, dashboard documentation and existing screenshot files were checked against the repository. |
| **What we can explain without AI** | The team can explain the Gold-to-dashboard flow, reporting grains, dashboard purpose and documented limitations. |

## 7. Blockers / Risks

| Blocker / Risk | Impact | Help Needed |
|---|---|---|
| A filtered-reconciliation screenshot is not currently present | Final visual-refinement evidence is incomplete | Capture the Power BI card under the same filter as the Gold check |
| PBIX internals are binary | GitHub Markdown review cannot independently verify every visual/filter configuration | Validate the final PBIX in Power BI Desktop |
| Final KPI reconciliation values are not recorded in this Markdown file | Dashboard values should not be invented | Record same-filter Gold-vs-Power-BI reconciliation after manual verification |

## 8. Next Week Preparation

- Week 10 should begin only after the Week 09 dashboard hand-off is accepted.
- Keep the Week 09 Gold-only dashboard stable.
- Move to the next guide-defined stage without changing the documented Week 09 evidence retrospectively.
