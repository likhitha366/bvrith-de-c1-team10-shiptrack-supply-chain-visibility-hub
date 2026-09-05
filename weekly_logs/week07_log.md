# Week 07 Log — Gold Layer Development

**Week:** 7
**Date range:** [Add dates]
**Team:** 10
**Project:** ShipTrack

---

## 1. Sprint Goal

The goal for Week 07 was to develop and validate the **Gold layer** of the ShipTrack data pipeline.
The team focused on creating business-ready datasets, applying business logic and data quality checks, and preparing trusted data for reporting and analytics.

---

## 2. Work Completed

| Task                                                              | Owner   | Status | Evidence                        |
| ----------------------------------------------------------------- | ------- | ------ | ------------------------------- |
| Developed Gold-layer datasets from the Trusted Silver data        | Team 10 | Done   | Gold-layer notebook             |
| Applied business rules and transformations required for analytics | Team 10 | Done   | Gold transformation code        |
| Implemented data quality checks on Gold datasets                  | Team 10 | Done   | DQ rules / notebook             |
| Validated Gold data for missing, duplicate, and invalid records   | Team 10 | Done   | Validation output / screenshots |
| Verified Gold tables and their final schema                       | Team 10 | Done   | Databricks table / notebook     |
| Updated project files and documentation in GitHub                 | Team 10 | Done   | GitHub repository               |

---

## 3. Key Decisions

* Gold datasets were designed to contain **business-ready and analytics-ready data** derived from the Trusted Silver layer.
* Business rules and transformations were applied before exposing the data for reporting and analysis.
* Data quality validation was performed to ensure that the Gold layer contains reliable and consistent records.
* The final Gold-layer schema was kept structured and easy to use for downstream dashboards and analytics.

---

## 4. Blockers / Risks

| Blocker                                                          | Impact                           | Help Needed                              |
| ---------------------------------------------------------------- | -------------------------------- | ---------------------------------------- |
| Some records required additional validation after transformation | Could affect Gold-layer accuracy | Review and validate transformation rules |
| Ensuring consistency between Silver and Gold schemas             | Possible schema mismatch         | Team review and testing                  |
| Data quality issues in transformed records                       | May affect reporting results     | Additional DQ validation                 |

---

## 5. Evidence Added to GitHub

* Gold-layer Databricks notebook updated.
* Gold transformation and business-rule code added.
* Data quality validation code/results added.
* Screenshots of Gold-layer outputs added.
* Final Gold table/schema validation evidence added.
* Week 07 project log updated.

---

## 6. AI Transparency Note

| Question                                | Response                                                                                                                                                                   |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Where AI helped**                     | AI was used to assist with drafting transformation logic, data quality checks, and documentation structure for the Gold layer.                                             |
| **What we changed after AI suggestion** | The suggested code and rules were modified according to our project's Gold-layer requirements, dataset structure, and team implementation.                                 |
| **What we verified manually**           | We manually checked the transformation results, column names, data types, business rules, duplicate records, missing values, and Gold-layer outputs in Databricks.         |
| **What we can explain without AI**      | We can explain the purpose of the Gold layer, Silver-to-Gold transformation process, business rules, data quality checks, validation process, and the final Gold datasets. |

---

## 7. Next Week Preparation

* Validate Gold datasets with additional test cases.
* Prepare Gold-layer data for dashboards and analytics.
* Review end-to-end flow from Bronze → Trusted Silver → Gold.
* Complete remaining documentation and evidence.
* Prepare the project for final review and demonstration.
