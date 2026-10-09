# Week 04 Log — Bronze Ingestion

**Week:** 4
**Date range:** 31 July – 6 August 2026
**Team:** 10
**Project:** ShipTrack – Supply Chain Visibility Hub

---

## 1. Sprint Goal

The goal of this sprint was to create Bronze tables from the raw source datasets while preserving the original data. We also added ingestion metadata and verified that the source record count matched the Bronze table record count.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Loaded raw source files into Databricks | Likhitha | Done | 02_bronze_ingestion.ipynb |
| Created Bronze Delta tables | Likhitha | Done | week04_bronze_table_created.png |
| Added metadata columns | Likhitha | Done | 02_bronze_ingestion.ipynb |
| Validated source count and Bronze count | Likhitha | Done | week04_bronze_counts.png |

---

## 3. Key Decisions

- Created Bronze tables without modifying the original source data.
- Added metadata columns to support data tracking and ingestion history.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| No major blockers | None | Not required |

---

## 5. Evidence Added to GitHub

- Updated `02_bronze_ingestion.ipynb`
- Added `week04_bronze_table_created.png`
- Added `week04_bronze_counts.png`
- Updated `week04_log.md`

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI helped explain the Bronze ingestion workflow and Databricks steps. |
| What we changed after AI suggestion | Updated the notebook structure and verified the ingestion process. |
| What we verified manually | Verified that the source record count matched the Bronze table record count and checked that the Bronze tables were created successfully. |
| What we can explain without AI | We can explain how raw data was loaded, Bronze tables were created, metadata was added, and validation was performed. |

---

## 7. Next Week Preparation

- Prepare for Silver layer transformations.
- Review Bronze tables before implementing data cleaning and transformations.
