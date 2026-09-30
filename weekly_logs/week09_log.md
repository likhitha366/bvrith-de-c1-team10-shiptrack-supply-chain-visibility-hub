# Week 09 Log — Dashboard Refinement and Insight Communication

**Week:** 9  
**Date:** September 2026  
**Team:** 10  
**Project:** ShipTrack — Supply Chain Visibility Hub

---

## 1. Sprint Goal

The goal for Week 09 was to carry the Week 08 Gold-only Power BI dashboard forward, refine its presentation and usability, and document evidence-backed dashboard observations without changing the underlying Gold business meaning.

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Carried the Week 08 PBIX forward | Team 10 | Done | `dashboard/Team10-PowerBI-Report.pbix` |
| Kept Gold tables as the reporting sources | Team 10 | Done | `dashboard/README.md`, Gold documentation |
| Reviewed dashboard structure and business-question mapping | Team 10 | Done | Dashboard documentation |
| Updated dashboard insight documentation | Team 10 | Done | `docs/dashboard_insights.md` |
| Updated dashboard README with Week 09 refinement rules | Team 10 | Done | `dashboard/README.md` |
| Updated Week 07 Gold definitions for downstream traceability | Team 10 | Done | `docs/gold_metrics_definition.md` |
| Added Week 09-specific screenshots | Team 10 | Not yet available | `screenshots/` |

## 3. Key Decisions

- Week 09 uses the existing Week 08 dashboard as the starting point rather than creating a new dashboard from scratch.
- The four approved Gold tables remain the reporting sources.
- Dashboard insights describe observable data patterns and do not claim causes that are not supported by the Gold data.
- Different Gold grains are kept conceptually separate; no unsafe relationship is introduced merely to force unrelated tables to share filters.

## 4. Dashboard / Gold Mapping

| Analysis | Owning Gold Table | Current Verified Rows |
|---|---|---:|
| Daily shipment trend | `gold_shipment_daily_metrics` | 180 |
| Carrier comparison | `gold_carrier_metrics` | 9 |
| Route comparison | `gold_route_metrics` | 100 |
| Hub comparison | `gold_hub_metrics` | 13 |

The row counts are the verified Gold outputs documented from Week 07 and are not claimed as new Week 09 measurements.

## 5. Evidence Added to GitHub

- `docs/dashboard_insights.md` — Week 09 insight and limitation documentation.
- `dashboard/README.md` — final source/model/refinement guidance.
- `docs/gold_metrics_definition.md` — Gold definitions carried through the reporting stage.
- `weekly_logs/week07_log.md`
- `weekly_logs/week08_log.md`
- `weekly_logs/week09_log.md`

Existing Week 08 dashboard screenshots remain in `screenshots/`. Week 09-specific refinement screenshots have not been invented or marked as present.

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
| Week 09-specific refinement screenshots are not currently present | Final visual-refinement evidence is incomplete | Capture genuine final/refinement screenshots from Power BI |
| PBIX internals are binary | GitHub Markdown review cannot independently verify every visual/filter configuration | Validate the final PBIX in Power BI Desktop |
| Final KPI reconciliation values are not recorded in this Markdown file | Dashboard values should not be invented | Record same-filter Gold-vs-Power-BI reconciliation after manual verification |

## 8. Next Week Preparation

- Week 10 should begin only after the Week 09 dashboard hand-off is accepted.
- Keep the Week 09 Gold-only dashboard stable.
- Move to the next guide-defined stage without changing the documented Week 09 evidence retrospectively.
