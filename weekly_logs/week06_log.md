# Week 06 Log — Data Quality Checks

**Week:** 6  
**Date range:** September 1–7, 2026  
**Team:** Team 10  
**Project:** ShipTrack – Supply Chain Visibility Hub

---

## 1. Sprint Goal

Implement a structured data-quality layer over the Silver data so that invalid shipment records can be identified, isolated, and prevented from contaminating downstream business metrics.

The shipment framework uses explicit DQ rule IDs and separates evaluated records into trusted and quarantine outputs.

---

## 2. Work Completed

| Task | Status | Evidence / Location |
|---|---|---|
| Define shipment DQ rules | Done | `docs/week06_dq_rule_mapping.md` |
| Implement shipment identity checks | Done | Week 6 DQ notebook / Databricks execution |
| Implement reference integrity checks | Done | Week 6 DQ notebook / Databricks execution |
| Implement timestamp chronology checks | Done | Week 6 DQ notebook / Databricks execution |
| Implement scan sequence checks | Done | Week 6 DQ notebook / Databricks execution |
| Implement route consistency checks | Done | Week 6 DQ notebook / Databricks execution |
| Implement delivery/status checks | Done | Week 6 DQ notebook / Databricks execution |
| Implement measure checks | Done | Week 6 DQ notebook / Databricks execution |
| Implement event/schema checks | Done | Week 6 DQ notebook / Databricks execution |
| Create trusted/quarantine outputs | Done for shipment framework | Databricks execution |
| Validate candidate reconciliation | Done for shipment framework | Databricks execution |
| Validate trusted/quarantine overlap | Done for shipment framework | Databricks execution |
| Document multi-rule quarantine handling | Done | `docs/data_quality_summary.md` |

---

## 3. Current Shipment DQ Results

The current executed shipment framework reports:

| Metric | Result |
|---|---:|
| Candidate distinct | 100,020 |
| Trusted | 99,857 |
| Quarantine | 163 |
| Reconciliation difference | 0 |
| Reconciliation result | PASS |
| Trusted ∩ Quarantine | 0 |

Rule-level failure counts:

| Rule ID | Failed Count |
|---|---:|
| DQ-SHP-001 | 32 |
| DQ-REF-001 | 34 |
| DQ-TIM-001 | 30 |
| DQ-SCN-001 | 28 |
| DQ-RTE-001 | 22 |
| DQ-DEL-001 | 20 |
| DQ-MEA-001 | 10 |
| DQ-EVT-001 | 0 |

Rule-level counts can exceed 163 because one quarantined shipment may fail multiple rules.

---

## 4. Key Decisions

- DQ rules were mapped to the actual Silver shipment columns and reference tables.
- Failed shipments are isolated rather than silently removed.
- One quarantine row is retained per `source_record_id`.
- `failed_rule_ids` stores all failed rule IDs for the record.
- `failure_details` stores the associated explanations.
- Expanded scan checks validate sequence start, sequence gaps, and timestamp ordering.
- A fixed scan `event_type` progression is not enforced because the current schema does not define a strict linear business progression.
- The DQ framework does not modify the Silver source tables.

---

## 5. Evidence Added to GitHub

- `docs/week06_dq_rule_mapping.md`
- `docs/data_quality_summary.md`
- `weekly_logs/week06_log.md`

Execution screenshots and notebook outputs remain Databricks-side evidence and should be added to `screenshots/` when available.

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI helped structure the DQ rule mapping, review the logic, and identify completeness gaps in chronology, scan sequencing, and route consistency. |
| What we changed after AI suggestion | The checks were aligned with the actual Silver schemas and the available route and scan-event fields. |
| What we verified manually | Table schemas, rule inputs, execution results, reconciliation, overlap, and sample quarantine records were checked in Databricks. |
| What we can explain without AI | We can explain the purpose of each DQ rule, how records are classified as trusted or quarantined, and why failed records must be isolated before downstream aggregation. |

---

## 7. Remaining Week 06 Work

The shipment DQ framework has executed successfully, but Week 6 is not yet fully closed.

Remaining items:

1. Complete and execute DQ coverage for the other required entities.
2. Implement and demonstrate controlled correction + replay for a quarantined record.
3. Capture final Databricks evidence for the completed Week 6 requirements.
4. Ensure the final Week 6 notebook(s) are committed to the GitHub repository.

These items should only be marked complete after execution evidence is available.

---

## 8. Next Week Preparation

- Use trusted outputs as the input boundary for Gold aggregations.
- Validate Gold row counts and metric definitions.
- Keep DQ evidence available for the final pipeline walkthrough.
