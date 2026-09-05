# Gold Metrics Definition

**Week:** 7
**Project:** ShipTrack
**Purpose:** Define dashboard-ready Gold tables and KPI formulas.

---

## 1. Gold Table Catalog

| Gold Table Name                 | Grain                                | Source Table(s)    | Purpose                                                        |
| ------------------------------- | ------------------------------------ | ------------------ | -------------------------------------------------------------- |
| `gold_shipment_summary_by_date` | One row per date and shipment status | `silver_shipments` | Daily shipment volume and status analysis                      |
| `gold_carrier_performance`      | One row per carrier                  | `silver_shipments` | Measure carrier shipment and delivery performance              |
| `gold_hub_performance`          | One row per hub                      | `silver_shipments` | Measure hub-level shipment, delivery and exception performance |
| `gold_zone_performance`         | One row per zone                     | `silver_shipments` | Analyze shipment and risk performance by zone                  |
| `gold_delivery_status_summary`  | One row per delivery status          | `silver_shipments` | Show shipment distribution across delivery statuses            |
| `gold_delay_analysis`           | One row per carrier, hub and zone    | `silver_shipments` | Identify areas with high shipment delays                       |
| `gold_severity_summary`         | One row per severity level           | `silver_shipments` | Analyze low, medium, high and critical shipment events         |
| `gold_shiptrack_kpis`           | One row for the complete dataset     | `silver_shipments` | Provide main ShipTrack dashboard KPIs                          |

---

## 2. KPI Definitions

| KPI Name                  | Formula                                                               | Grain                | Dashboard Page       | Notes                                     |
| ------------------------- | --------------------------------------------------------------------- | -------------------- | -------------------- | ----------------------------------------- |
| Total Shipments           | `COUNT(DISTINCT shipment_id)`                                         | Overall              | Overview             | Total unique shipments                    |
| Delivered Shipments       | `COUNT(DISTINCT shipment_id)` where `status = 'Delivered'`            | Overall              | Overview             | Successfully delivered shipments          |
| Delayed Shipments         | `COUNT(DISTINCT shipment_id)` where `status = 'Delayed'`              | Overall              | Delivery Performance | Shipments currently delayed               |
| Exception Shipments       | `COUNT(DISTINCT shipment_id)` where `status = 'Exception'`            | Overall              | Risk / Exceptions    | Shipments with delivery exceptions        |
| High-Risk Shipments       | `COUNT(DISTINCT shipment_id)` where `severity IN ('HIGH','CRITICAL')` | Overall              | Risk / Exceptions    | Shipments requiring attention             |
| Delivery Rate             | `Delivered Shipments / Total Shipments × 100`                         | Overall              | Overview             | Percentage of shipments delivered         |
| Delay Rate                | `Delayed Shipments / Total Shipments × 100`                           | Overall              | Delivery Performance | Percentage of shipments delayed           |
| Shipment Count            | `COUNT(DISTINCT shipment_id)`                                         | Daily                | Shipment Overview    | Daily shipment volume                     |
| Carrier Shipments         | `COUNT(DISTINCT shipment_id)`                                         | Carrier              | Carrier Performance  | Total shipments handled by each carrier   |
| Carrier Delayed Shipments | `COUNT(DISTINCT shipment_id)` where `status = 'Delayed'`              | Carrier              | Carrier Performance  | Delayed shipments by carrier              |
| Hub Shipments             | `COUNT(DISTINCT shipment_id)`                                         | Hub                  | Hub Performance      | Total shipments handled by each hub       |
| Zone Shipments            | `COUNT(DISTINCT shipment_id)`                                         | Zone                 | Zone Performance     | Total shipments associated with each zone |
| Delay Percentage          | `Delayed Shipments / Total Shipments × 100`                           | Carrier / Hub / Zone | Delay Analysis       | Percentage of delayed shipments           |
| Event Count               | `COUNT(*)`                                                            | Severity             | Risk / Exceptions    | Number of events by severity              |

---

## 3. Gold Table Details

### 3.1 `gold_shipment_summary_by_date`

This table provides daily shipment activity grouped by delivery status.

**Main fields:**

* `event_date`
* `status`
* `record_count`
* `unique_shipments`

**Purpose:**
Used to create daily shipment-volume and status-trend visualizations.

---

### 3.2 `gold_carrier_performance`

This table measures the performance of each carrier.

**Main fields:**

* `carrier_id`
* `total_shipments`
* `delivered_shipments`
* `delayed_shipments`
* `high_risk_events`

**Purpose:**
Used to compare carriers and identify carriers with higher delivery delays or risk events.

---

### 3.3 `gold_hub_performance`

This table provides performance metrics for each hub.

**Main fields:**

* `hub_id`
* `total_shipments`
* `delivered_shipments`
* `delayed_shipments`
* `exception_shipments`

**Purpose:**
Used to identify high-performing and problematic hubs.

---

### 3.4 `gold_zone_performance`

This table summarizes shipment activity by zone.

**Main fields:**

* `zone_id`
* `total_shipments`
* `delivered_shipments`
* `delayed_shipments`
* `high_risk_shipments`

**Purpose:**
Used for geographical or operational zone analysis.

---

### 3.5 `gold_delivery_status_summary`

This table summarizes the distribution of shipment statuses.

**Main fields:**

* `status`
* `shipment_count`
* `percentage_of_shipments`

**Purpose:**
Used for status charts and delivery-status dashboards.

---

### 3.6 `gold_delay_analysis`

This table identifies shipment delays across carriers, hubs and zones.

**Main fields:**

* `carrier_id`
* `hub_id`
* `zone_id`
* `total_shipments`
* `delayed_shipments`
* `delay_percentage`

**Purpose:**
Used to identify areas where shipment delays are highest.

---

### 3.7 `gold_severity_summary`

This table summarizes shipment events according to severity.

**Main fields:**

* `severity`
* `event_count`
* `affected_shipments`

**Purpose:**
Used to monitor operational risk and critical shipment events.

---

### 3.8 `gold_shiptrack_kpis`

This is the main KPI table for the ShipTrack dashboard.

**Main fields:**

* `total_shipments`
* `delivered_shipments`
* `delayed_shipments`
* `exception_shipments`
* `high_risk_shipments`

**Purpose:**
Provides a single source for the main dashboard KPI cards.

---

## 4. Validation Checks

Before using Gold tables in Power BI, verify:

* Gold row counts are reasonable.
* No unexpected NULL values exist in important dashboard fields.
* `shipment_id` values are correctly represented in the Silver source.
* KPI totals match manual spot checks.
* Delivered, delayed and exception counts are logically consistent.
* Delivery rate is between 0% and 100%.
* Delay rate is between 0% and 100%.
* Carrier, hub and zone IDs are available for their respective Gold tables.
* High-risk shipments contain only `HIGH` or `CRITICAL` severity records.
* Power BI connects to Gold outputs only.
* Metric definitions are documented clearly.
* Gold tables are refreshed after the Trusted Silver layer is updated.

---

## 5. Dashboard Mapping

The Gold tables can support the following ShipTrack dashboard pages:

### Overview Dashboard

* Total Shipments
* Delivered Shipments
* Delayed Shipments
* Exception Shipments
* Delivery Rate
* Delay Rate

### Carrier Performance

* Total shipments by carrier
* Delivered shipments by carrier
* Delayed shipments by carrier
* High-risk events by carrier

### Hub & Zone Performance

* Shipments by hub
* Shipments by zone
* Delayed shipments by hub
* Delayed shipments by zone
* High-risk shipments by zone

### Risk & Exceptions

* High-risk shipments
* Critical events
* Delivery exceptions
* Delay percentage
* Severity distribution

---

## 6. Metric Calculation Principles

All Gold metrics are calculated from the Trusted Silver table:

`silver_shipments`

The Gold layer is intended to contain aggregated, dashboard-ready data. Power BI should consume the Gold tables rather than directly querying the raw or Bronze data.

The primary business key for shipment-level calculations is:

`shipment_id`

This prevents duplicate shipment records from incorrectly increasing shipment-level KPI values.

---

## 7. Final Data Flow

```text
Raw Shipment Data
       |
       v
Bronze Layer
       |
       v
Trusted Silver
silver_shipments
       |
       v
Gold Aggregations
       |
       +----------------------+
       |          |           |
       v          v           v
   Carrier      Hub/Zone    Delivery
   Metrics      Metrics     Metrics
       |          |           |
       +----------+-----------+
                  |
                  v
             ShipTrack KPIs
                  |
                  v
             Power BI
             Dashboard
```

---

**Status:** Week 7 Gold metric definitions completed.
