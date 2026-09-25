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
| DQ-DEL-001 | Delivery/status consistency | 20 | Inconsistent delivery and status fields can affect shipment outcome reporting. |
| DQ-MEA-001 | Measures | 10 | Invalid shipment measures can affect operational and financial metrics. |
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

Other-entity DQ checks and controlled correction/replay are separate Week 6 work items and should only be marked complete after their execution evidence is captured.
