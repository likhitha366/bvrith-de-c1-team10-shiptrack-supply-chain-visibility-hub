# Week 05 Log — Silver Transformations

**Week:** 5
**Date range:** 7 August – 13 August 2026
**Team:** 10
**Project:** ShipTrack: Supply Chain Visibility Hub

---

## 1. Sprint Goal

Standardize and transform the Bronze-layer data into clean and structured Silver tables.
Create six Silver tables for carriers, exceptions, hubs, routes, scan events, and shipments with appropriate data types, standardized fields, and duplicate handling.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|------|-------|--------|----------|
| Silver transformation for Scan Events | likhitha | Done | `03_silver_transformations.ipynb` |
| Silver transformation for Shipments | likhitha| Done | `03_silver_transformations.ipynb` |
| Silver transformation for Carriers | shivani | Done | `03_silver_transformations.ipynb` |
| Silver transformation for Routes | shivani | Done | `03_silver_transformations.ipynb` |
| Silver transformation for Hubs | Meenakshi | Done | `03_silver_transformations.ipynb` |
| Silver transformation for Exceptions | Meenakshi | Done | `03_silver_transformations.ipynb` |
| Silver table validation and row-count checks | Meenakshi | Done | Databricks screenshots |

---

## 3. Key Decisions

- Created one Silver table corresponding to each Bronze table.
- Standardized scan event fields by renaming columns and converting event time into timestamp and date fields.
- Standardized shipment status using lowercase values.
- Removed duplicate records during Silver transformations where applicable.
- Stored the transformed datasets as managed Silver tables.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---------|--------|-------------|
| Generic Silver template contained columns such as `amount` and `reference_id` that were not present in the project data | Required modification of the template to match the actual Bronze schema | Verified Bronze schemas and modified transformations accordingly |
| Initial validation query referenced the non-existent `amount` column | SQL validation query failed | Replaced the query with a status-based record-count query |

---

## 5. Evidence Added to GitHub

- `03_silver_transformations.ipynb`
- Silver transformation screenshots
- Silver schema screenshots
- Silver row-count screenshots
- SQL validation results

---

## 6. AI Transparency Note

| Question | Response |
|----------|----------|
| Where AI helped | AI helped adapt the generic Silver transformation template to the actual Bronze table schemas and suggested suitable validation queries. |
| What we changed after AI suggestion | We replaced generic fields such as `amount`, `reference_id`, and `event_timestamp` with fields that actually exist in our Bronze data. |
| What we verified manually | Bronze table names, column names, schemas, Silver table creation, row counts, and SQL query results were manually verified in Databricks. |
| What we can explain without AI | We can explain the Bronze-to-Silver transformation process, schema standardization, duplicate handling, Silver table creation, and validation process. |

---

## 7. Next Week Preparation

- Review and validate all Silver tables.
- Prepare the Silver data for Gold-layer transformations.
- Identify relationships between shipments, scan events, routes, hubs, carriers, and exceptions.
- Begin designing analytics-ready Gold tables and KPIs.
