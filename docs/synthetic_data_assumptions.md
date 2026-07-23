# Synthetic Data Assumptions

**Project:** ShipTrack – Supply Chain Visibility Hub  
**Week:** 2  
**Purpose:** Document the assumptions used for generating synthetic logistics and supply chain data.

---

# 1. Synthetic Data Boundary

This project uses **synthetically generated logistics and supply chain data** for educational purposes only.

The dataset does **not** represent any real logistics company, customer, shipment, warehouse, carrier, employee, or business operation.

All shipment IDs, carrier names, hubs, routes, tracking events, and exception records are fictional and are generated solely for learning Data Engineering concepts.

---

# 2. Domain Assumptions

| Area | Assumption |
|------|------------|
| Geography / Scope | Shipments move between fictional hubs located across major regions of India (North, South, East, West, and Central). |
| Time Period | Shipment records and tracking events are generated between **July 2026 and September 2026**. |
| Source Systems | Data originates from multiple operational systems including Shipment Management, Hub Management, Carrier Management, Route Planning, Scan Tracking, Exception Management, and Streaming Event Generator. |
| Event Types | Shipment lifecycle events include Pickup, Hub Arrival, Hub Departure, In Transit, Out for Delivery, Delivered, Delayed, Returned, Cancelled, and Exception events. |
| Reference Data | Master reference datasets include Hubs, Carriers, Routes, Service Levels, Transport Modes, Shipment Statuses, and Exception Categories. |

---

# 3. Data Volume Assumptions

| File | Approximate Rows | Reason |
|------|-----------------:|--------|
| shipments.parquet | ~5,000 | Core shipment records for analytics and KPI calculations |
| hubs.json | ~25 | Warehouse and distribution hub master data |
| carriers.csv | ~15 | Logistics carrier reference information |
| routes.csv | ~120 | Transportation routes connecting hubs |
| scan_events.csv | ~25,000 | Historical shipment scan records across the shipment lifecycle |
| exceptions.csv | ~800 | Shipment exception and delay records |
| streaming/scan_event.json | Incremental event drops | Simulates real-time shipment tracking using NDJSON streaming files |

---

# 4. Controlled Data Quality Issues

To support Data Quality (DQ) validation during later stages of the project, controlled data issues are intentionally introduced.

| Issue Type | Approx. Share | Why Include It |
|------------|--------------:|----------------|
| Duplicate Shipment or Event IDs | 0.2%–0.5% | Tests duplicate detection and uniqueness validation |
| Missing Mandatory Values | 1%–3% | Tests completeness rules |
| Invalid Foreign Keys | 0.5%–1% | Tests referential integrity between shipments, hubs, carriers, and routes |
| Invalid Numeric Values | 0.1%–0.5% | Tests measurement and range validation |
| Timestamp Inconsistencies | 0.1%–0.3% | Tests shipment lifecycle chronology |
| Invalid Shipment Status Transitions | 0.2%–0.5% | Tests shipment lifecycle validation |
| Route or Carrier Mismatch | 0.2%–0.5% | Tests business rule validation |
| Malformed Streaming Events | Small controlled set | Tests streaming schema validation and quarantine logic |

---

# 5. Manual Verification

Before using the generated dataset, the team must verify that:

- Source files are successfully generated in the expected formats (Parquet, CSV, JSON, and NDJSON).
- Row counts are within the expected range.
- Primary Key fields contain unique values where applicable.
- Foreign Key relationships are valid across shipments, hubs, carriers, routes, scans, and exceptions.
- Dates and timestamps follow realistic shipment lifecycles.
- Shipment statuses follow valid business transitions.
- Controlled data quality issues exist but remain a very small percentage of the dataset.
- Sample records accurately represent shipment movement across the logistics network.
- Streaming event files follow the expected schema and ordering.
- The dataset is suitable for Bronze, Silver, Gold, Data Quality, and Power BI pipeline development.

---

# 6. Notes

- All datasets are synthetically generated and contain no real customer or business information.
- Data has been designed to support Bronze, Silver, Trusted Silver, Quarantine, Gold, and Streaming layers of the ShipTrack Data Engineering pipeline.
- Controlled data quality issues are intentionally included to validate Data Quality rules and reconciliation during later project stages.
