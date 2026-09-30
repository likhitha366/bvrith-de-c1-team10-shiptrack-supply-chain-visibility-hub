# Gold Metrics Definition

**Week:** 7  
**Project:** ShipTrack  
**Purpose:** Define the business-ready Gold tables, their grains, sources, and KPI usage for downstream reporting.

---

## 1. Gold Table Catalog

| Gold Table | Grain | Source | Purpose |
|---|---|---|---|
| `gold_shipment_daily_metrics` | One row per booking date | `trusted_shipments` | Daily shipment volume and delivery-performance metrics |
| `gold_carrier_metrics` | One row per carrier | `trusted_shipments` | Carrier-level shipment and delivery performance |
| `gold_route_metrics` | One row per route | `trusted_shipments` | Route-level delivery performance |
| `gold_hub_metrics` | One row per hub | `trusted_shipments` | Hub-level shipment flow and delivery performance |

All Gold outputs are downstream of the Trusted shipment data produced by the Week 06 data-quality process.

## 2. KPI Definitions

| KPI | Definition |
|---|---|
| Total shipments | Count of trusted shipment records included in the relevant Gold aggregation |
| Delivered shipments | Shipment records with a completed delivery outcome/status according to the implemented Gold logic |
| Delayed deliveries | Shipment records classified as delayed according to the implemented Gold logic |
| Delivery rate | Delivered shipments / total shipments × 100 |
| On-time delivery rate | On-time delivered shipments / eligible delivered shipments × 100, according to the implemented Gold logic |
| Average delivery hours | Average elapsed delivery time using the timestamps implemented in the Gold transformation |
| Total freight | Aggregated freight amount from trusted shipment records |
| Hub flow counts | Shipment flow counts aggregated by hub |

The Gold aggregation notebook remains the source of truth for the exact SQL expressions and output columns.

## 3. Implemented Gold Outputs

### `gold_shipment_daily_metrics`

**Grain:** One row per booking date.  
**Purpose:** Daily shipment volume and delivery-performance trends.

### `gold_carrier_metrics`

**Grain:** One row per carrier.  
**Purpose:** Carrier shipment volume, delivery performance, timing and freight analysis.

### `gold_route_metrics`

**Grain:** One row per route.  
**Purpose:** Route shipment volume and delivery-performance analysis.

### `gold_hub_metrics`

**Grain:** One row per hub.  
**Purpose:** Hub shipment flow and delivery-performance analysis.

## 4. Verified Week 07 Outputs

| Gold Table | Verified Rows |
|---|---:|
| `gold_shipment_daily_metrics` | 180 |
| `gold_carrier_metrics` | 9 |
| `gold_route_metrics` | 100 |
| `gold_hub_metrics` | 13 |

These counts describe the executed Week 07 outputs and may change if the upstream Trusted dataset changes.

## 5. Validation Requirements

- Gold tables are created successfully.
- Gold tables use the Trusted shipment data rather than raw or untrusted Silver data.
- Output row counts match the declared aggregation grain.
- KPI percentages remain within logical bounds.
- Aggregations do not introduce duplicate rows at their declared grain.
- Downstream Power BI reporting consumes Gold outputs only.

## 6. Data Flow

```text
Raw Data
   ↓
Bronze
   ↓
Silver
   ↓
Week 06 DQ Evaluation
   ↓
Trusted Silver
   ↓
Gold Aggregations
   ├── Daily Shipment Metrics
   ├── Carrier Metrics
   ├── Route Metrics
   └── Hub Metrics
   ↓
Power BI / Reporting
```

## 7. Downstream Use

The Gold outputs are the approved reporting layer used for the Week 08 Power BI dashboard and the Week 09 dashboard refinement and insight work. Power BI should not bypass Gold by connecting directly to raw or Silver detail data.

**Status:** Week 07 Gold metric definitions documented and carried forward through Week 09 reporting work.
