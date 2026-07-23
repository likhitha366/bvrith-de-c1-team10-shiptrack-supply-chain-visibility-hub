# Week 02 Log — Meet the Data: Contracts, Grains and Checksums

**Week:** 2  
**Date Range:** 21 July 2026 – 27 July 2026  
**Team:** Team 10  
**Project:** ShipTrack – Supply Chain Visibility Hub

---

## 1. Sprint Goal

The objective of Week 02 was to understand the ShipTrack dataset by identifying all source files, documenting their schemas, defining primary and foreign keys, understanding the business grain of each dataset, and preparing the documentation required before starting the Bronze ingestion layer.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|------|-------|--------|----------|
| Reviewed ShipTrack Project Playbook | Team 10 | Done | Project Playbook PDF |
| Identified all source datasets and formats | Team 10 | Done | `docs/data_dictionary.md` |
| Documented fields, data types, and descriptions | Team 10 | Done | `docs/data_dictionary.md` |
| Defined Primary Keys and Foreign Keys | Team 10 | Done | `docs/data_dictionary.md` |
| Documented synthetic data assumptions | Team 10 | Done | `docs/synthetic_data_assumptions.md` |
| Prepared sample raw datasets | Team 10 | Done | `data_sample/raw/` |
| Studied dataset relationships and business grain | Team 10 | Done | Project Documentation |
| Updated Week 02 log | Team 10 | Done | `weekly_logs/week02_log.md` |

---

## 3. Key Decisions

- Used the official ShipTrack dataset and source structure provided in the project.
- Preserved the original business grain of each dataset.
- Documented all source files before implementing the Bronze layer.
- Used only synthetic logistics data for educational purposes.
- Followed the official repository naming conventions.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|----------|--------|-------------|
| Understanding relationships between shipment, scan, and exception datasets | Medium | Reviewed project documentation to understand data relationships |
| Identifying correct primary and foreign keys | Low | Cross-verified using dataset documentation |
| Understanding streaming event structure | Low | Studied the project playbook before documentation |

---

## 5. Evidence Added to GitHub

- Updated `docs/data_dictionary.md`
- Updated `docs/synthetic_data_assumptions.md`
- Added sample files to `data_sample/raw/`
- Updated `weekly_logs/week02_log.md`

---

## 6. AI Transparency Note

| Question | Response |
|----------|----------|
| Where AI helped | Assisted in preparing the Data Dictionary, Synthetic Data Assumptions, and Week 02 documentation using the project requirements. |
| What we changed after AI suggestion | Verified the generated documentation and modified it to match the ShipTrack project structure and dataset. |
| What we verified manually | Source files, field names, keys, business grain, and dataset relationships. |
| What we can explain without AI | Project overview, dataset structure, source files, keys, business grain, and Week 02 documentation. |

---

## 7. Next Week Preparation

- Begin Bronze layer data ingestion.
- Load all source files into Bronze tables.
- Preserve raw data without transformations.
- Add ingestion metadata (`source_file`, `ingestion_ts`, `run_id`, and `source_record_id`).
- Validate source-to-Bronze reconciliation.
- Update the Bronze ingestion notebook and documentation.
