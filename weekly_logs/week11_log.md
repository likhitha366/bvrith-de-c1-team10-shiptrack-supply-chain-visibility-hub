# Week 11 Log — Integration and Evidence Clean-up

**Week:** 11  
**Date range:** 6 October – 12 October 2026  
**Team:** 10  
**Project:** ShipTrack: Supply Chain Visibility Hub

---

## 1. Sprint Goal

Bring the repository to one consistent story from raw files to dashboard and stream: complete the pipeline walkthrough and references, make the weekly logs and screenshots agree with the notebooks, and list what is still open before the final week.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Wrote the pipeline walkthrough (run order, architecture, limitations, reproduction steps) | R. Meenakshi Reddy | Done | `docs/pipeline_walkthrough.md` |
| Completed the references | R. Meenakshi Reddy | Done | `docs/references.md` |
| Cleaned `README.md` and rewrote the notebook and screenshot indexes | R. Meenakshi Reddy | Done | `README.md`, `notebooks/README.md`, `screenshots/README.md` |
| Corrected the Week 7 to 9 logs to the rebuilt Gold layer and added date ranges | R. Meenakshi Reddy | Done | `weekly_logs/week07_log.md` to `week09_log.md` |
| Renamed the three refined dashboard captures to Week 9 and three other misnamed screenshots | R. Meenakshi Reddy | Done | `screenshots/week09_powerbi_*.png`, `screenshots/week06_dq_notebook.png`, `screenshots/week08_databricks_dashboard_draft*.png` |
| Pointed the dashboard documents at the file that is in the repository | R. Meenakshi Reddy | Done | `dashboard/README.md`, `docs/dashboard_insights.md` |
| Added source seeding and a results cell to the Week 10 notebook | R. Meenakshi Reddy | Done | `notebooks/07_streaming_simulation.ipynb` sections 2 and 22.1 |
| Run the Week 10 notebook in Databricks and capture `week10_*` screenshots | B. Likhitha, R. Meenakshi Reddy, G. Shivani | In progress | `weekly_logs/week10_log.md` |
| Rerun the exceptions data-quality cell and update the reconciliation | Team 10 | Not started | `docs/data_quality_summary.md` section 7 |
| Replace summed-rate KPI cards with measures and capture a filtered reconciliation | Team 10 | Not started | `dashboard/README.md` section 8 |

---

## 3. Key Decisions

- Past logs are corrected with a dated note instead of being rewritten silently, so a reviewer can see what changed and when.
- Screenshots are renamed to say what they show; the images themselves are not edited.
- Known gaps are written down in `docs/pipeline_walkthrough.md` section 3 and are not presented as complete.
- No result is recorded for the Week 10 stream until the notebook has been run in Databricks.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Week 10 notebook not yet run in Databricks | No streaming results or screenshots; the final demo has no live evidence | Run the notebook and paste the output of cell 22.1 into the Week 10 log |
| Exceptions data-quality reconciliation still shows a difference of 2 | One data-quality table is marked FAIL | Rerun the corrected cell |
| Some KPI cards sum rate columns | Cards do not match the governed Gold values | Add measures in Power BI Desktop and re-capture the pages |

---

## 5. Evidence Added to GitHub

- `docs/pipeline_walkthrough.md`
- `docs/references.md`
- `README.md`, `notebooks/README.md`, `screenshots/README.md`
- `weekly_logs/week04_log.md`, `week05_log.md`, `week07_log.md`, `week08_log.md`, `week09_log.md` (dates and corrections)
- `dashboard/README.md`, `docs/dashboard_insights.md`
- `docs/synthetic_data_assumptions.md` (volumes actually loaded)
- Renamed screenshots listed in `screenshots/README.md`

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI audited the repository against the weekly evidence list, drafted the pipeline walkthrough, references and README indexes, proposed the screenshot renames after viewing each image, and drafted the corrections to the Week 7 to 9 logs from the saved notebook outputs. |
| What we changed after AI suggestion | To be completed by the team before the Week 11 review. |
| What we verified manually | To be completed by the team before the Week 11 review. |
| What we can explain without AI | To be completed by the team before the Week 11 review. |

---

## 7. Next Week Preparation

- Finish the Databricks run of the Week 10 notebook and record its results.
- Write `final_submission/final_report.md`, the demo script and the team contribution note.
- Rehearse the walkthrough in `docs/pipeline_walkthrough.md` section 4 end to end.
