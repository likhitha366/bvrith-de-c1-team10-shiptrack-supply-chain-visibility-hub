# Data Quality Summary

**Project:** ShipTrack – Supply Chain Visibility Hub  
**Week:** 6

**Purpose:** Validate Silver shipment data using explicit data-quality rules, isolate failed records, and document their downstream impact.

---

## 1. Shipment DQ Rule Results

The current Week 6 shipment framework evaluates **100,020** candidate shipment records.

| Rule ID | Rule Name | Failed Count | Business Impact |
|---|---|---:|---|
| DQ-SHP-001 | Shipment identity | 32 | Missing or invalid identity fields can make shipment records unreliable or difficult to trace. |
| DQ-REF-001 | Reference integrity | 34 | Invalid hub, carrier, or route references can produce incorrect joins and reporting. |
| DQ-TIM-001 | Chronology | 30 | Incorrect timestamp relationships can distort delivery-duration and on-time metrics. |
| DQ-SCN-001 | Scan sequence | 28 | Invalid scan sequencing can affect shipment-event tracking and event chronology. |
| DQ-RTE-001 | Route consistency | 22 | Route/hub or route-attribute mismatches can misrepresent shipment routing. |
| DQ-DEL-001 | Delivery/status consistency | 10 | Inconsistent delivery and status fields can affect shipment outcome reporting. |
| DQ-MEA-001 | Measures | 20 | Invalid shipment measures can affect operational and financial metrics. |
| DQ-EVT-001 | Event/schema | 0 | No failures were reported for this rule in the current execution. |

> Rule failure counts are **rule-level counts**. A single shipment can fail more than one rule, so these counts do not sum to the number of quarantined records.

---

## 2. Candidate / Trusted / Quarantine Reconciliation

Current shipment execution:

- Candidate distinct records: **100,020**
- Trusted records: **99,857**
- Quarantine records: **163**
- Reconciliation difference: **0**
- Reconciliation result: **PASS**
- Trusted ∩ Quarantine overlap: **0**

Therefore:

`100,020 = 99,857 + 163`

The framework keeps failed records in quarantine rather than silently dropping them.

---

## 3. Multi-Rule Failure Handling

Quarantine uses one row per `source_record_id` and stores:

- `failed_rule_ids` as an `ARRAY<STRING>`
- `failure_details` as the corresponding rule explanations

This allows a shipment that fails multiple checks to remain a single quarantine record while retaining all detected failures.

Examples observed in the current execution include combinations such as:

- `DQ-REF-001` + `DQ-RTE-001`
- `DQ-SCN-001` + `DQ-MEA-001`

---

## 4. Handling of Failed Records

Failed records are isolated into the quarantine output for review. The Silver source tables are not modified by the DQ evaluation.

A later controlled-correction/replay step is required before Week 6 can be considered fully complete.

---

## 5. Business Impact

The most important downstream risks are:

- Reference failures can cause incorrect joins between shipments and reference entities.
- Timestamp failures can affect delivery-duration and on-time calculations.
- Scan-sequence failures can affect event-level shipment tracking.
- Route inconsistencies can affect route and hub performance reporting.
- Measure failures can affect operational and financial aggregations.

Gold metrics should consume trusted data rather than the full Silver shipment population.

---

## 6. Scope Notes

The shipment DQ framework contains eight rule IDs. The current implementation includes expanded chronology, scan-sequence, and route-consistency checks.

For scan events, a fixed `event_type` progression is not enforced because the available event types do not define a strict linear business progression in the current schema.

Controlled correction/replay is a separate Week 6 work item and is marked complete only after its execution evidence is captured.

---

## 7. Other Entities — Executed Results

Source: Part B of `notebooks/04_data_quality_checks.ipynb` (run of 24 September 2026). Each entity is routed to `trusted_*` or `quarantine_*`.

| Entity | Rules | Candidate | Trusted | Quarantine | Difference | Result | Overlap |
|---|---|---:|---:|---:|---:|---|---:|
| Hubs | DQ-HUB-001 identity, DQ-HUB-002 enum, DQ-HUB-003 dates | 14 | 14 | 0 | 0 | PASS | 0 |
| Carriers | DQ-CAR-001 identity, DQ-CAR-002 enum, DQ-CAR-003 dates | 10 | 10 | 0 | 0 | PASS | 0 |
| Routes | DQ-RT-001 identity, DQ-RT-002 reference, DQ-RT-003 enum, DQ-RT-004 dates, DQ-RT-005 measures | 107 | 103 | 4 | 0 | PASS | 0 |
| Scan events | DQ-SCN-001 identity, DQ-SCN-002 enum, DQ-SCN-003 timestamp | 710,666 | 710,666 | 0 | 0 | PASS | 0 |
| Exceptions | DQ-EXC-001 identity, DQ-EXC-002 reference, DQ-EXC-003 enum, DQ-EXC-004 chronology | 18,352 | 18,330 | 24 | -2 | FAIL | 0 |

### Open item — exceptions reconciliation

The exceptions run shows Trusted + Quarantine = 18,354 against 18,352 Candidate rows. The join to shipments in that run multiplied exception rows whose `shipment_id` appears twice in `silver_shipments`. The notebook cell now joins to `SELECT DISTINCT shipment_id`; the cell must be rerun and this table updated with the new result before Week 6 is closed. `05_gold_aggregations.ipynb` and `06_powerbi_export.ipynb` must be rerun afterwards because `trusted_exceptions` feeds `gold_fact_shipment_exception`.

### Rule-ID note

The entity rule IDs above are team-defined. They cover the checks that the approved catalogue assigns to these entities under `DQ-REF-001`, `DQ-RTE-001`, `DQ-MEA-001`, `DQ-TIM-001` and `DQ-SCN-001`.
