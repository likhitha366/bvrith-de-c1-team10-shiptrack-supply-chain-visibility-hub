# Week 08 Log — Power BI Dashboard Draft

**Week:** 8  
**Date range:** 25 September 2026  
**Team:** 10  
**Project:** ShipTrack — Supply Chain Visibility Hub

---

## 1. Sprint Goal

The goal for Week 08 was to begin the reporting/dashboard layer using the Week 07 Gold outputs and create the first Power BI dashboard draft.

The repository should contain the dashboard file and supporting documentation while keeping the downstream flow based on Gold data.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Prepared the Week 07 Gold layer for dashboard use | Team 10 | Done | `docs/gold_metrics_definition.md`, Gold aggregation work |
| Added the Power BI dashboard file to the repository | Team 10 | Done | `dashboard/Team10-PowerBI-Report.pbix` |
| Maintained the dashboard folder structure and usage guidance | Team 10 | Done | `dashboard/README.md` |
| Added the dashboard-insights documentation template | Team 10 | In progress | `docs/dashboard_insights.md` |
| Added final Week 08 dashboard screenshots | Team 10 | Not yet verified | `screenshots/` |
| Completed dashboard insight write-up and KPI validation | Team 10 | In progress | `docs/dashboard_insights.md` |

The Power BI file is present in GitHub as `dashboard/Team10-PowerBI-Report.pbix`. The repository dashboard guidance states that Power BI should use Gold outputs and that dashboard screenshots and insights must also be documented.

---

## 3. Key Decisions

- Continue the **Trusted Silver → Gold → Power BI** flow established in Weeks 06–07.
- Use the implemented Gold tables as the reporting layer rather than connecting Power BI directly to raw source files.
- Keep the PBIX file in the `dashboard/` folder as the current Week 08 dashboard artifact.
- Treat dashboard screenshots, KPI reconciliation, and written insights as remaining evidence work rather than marking them complete without verification.

---

## 4. Blockers / Risks

| Blocker / Risk | Impact | Help Needed |
|---|---|---|
| Dashboard screenshots are not yet confirmed as complete Week 08 evidence | The dashboard cannot yet be fully demonstrated from GitHub evidence | Capture and upload final dashboard screenshots |
| `docs/dashboard_insights.md` still contains placeholders | Dashboard story and insights are not fully documented | Replace placeholders with verified observations from the actual dashboard |
| PBIX internals cannot be validated from the GitHub connector because `.pbix` is a binary file | Connection details and visual configuration cannot be independently confirmed here | Verify the Power BI model manually in Power BI Desktop |
| Gold export evidence is not currently represented by populated files under `data_sample/gold_exports/` | Reproducibility of the dashboard input data is not fully demonstrated in GitHub | Add the approved small Gold sample/export evidence if required by the project rules |

---

## 5. Evidence Added to GitHub

- `dashboard/Team10-PowerBI-Report.pbix` — Power BI dashboard artifact added.
- `dashboard/README.md` — dashboard storage and validation guidance.
- `docs/dashboard_insights.md` — dashboard documentation template.
- Week 07 Gold documentation and aggregation work remain available as the upstream reporting evidence.

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| **Where AI helped** | AI was used to review the repository state, identify completed Week 08 artifacts, and structure the weekly progress documentation. |
| **What we changed after AI suggestion** | The log was updated to distinguish verified repository evidence from work that still requires manual confirmation. |
| **What we verified manually** | The GitHub repository contains the Week 08 PBIX artifact, dashboard README, and dashboard-insights document. The PBIX itself was not inspected internally because it is a binary file. |
| **What we can explain without AI** | We can explain the Gold-to-dashboard flow, the purpose of the Power BI artifact, and the remaining screenshot/insight validation work. |

---

## 7. Next Week Preparation

- Open the PBIX in Power BI Desktop and verify that all visuals use the intended Gold outputs.
- Validate KPI totals against the implemented Gold tables.
- Capture clear dashboard screenshots for GitHub evidence.
- Replace the placeholders in `docs/dashboard_insights.md` with verified dashboard observations.
- Prepare the Week 09 dashboard-refinement log only after the Week 08 evidence is complete.
