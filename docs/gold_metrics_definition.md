# Gold Metrics Definition

**Week:** 7  
**Project:** ShipTrack  
**Purpose:** Define the business-ready Gold tables, grains, and KPI calculations used for downstream reporting and analytics.

---

## 1. Gold Table Catalog

| Gold Table | Grain | Source | Purpose |
|---|---|---|---|
| `gold_shipment_daily_metrics` | One row per booking date | `trusted_shipments` | Daily shipment volume and delivery-performance metrics |
| `gold_carrier_metrics` | One row per carrier | `trusted_shipments` | Carrier-level shipment and delivery performance |
| `gold_route_metrics` | One row per route | `trusted_shipments` | Route-level shipment and delivery performance |
| `gold_hub_metrics` | One row per hub | `trusted_shipments` | Hub-level shipment flow and delivery performance |

Gold is built from **Trusted Silver** so that records that failed the Week 06 shipment DQ framework are not included in downstream analytics.

---

## 2. Gold Table Details

### 2.1 `gold_shipment_daily_metrics`

**Grain:** One row per booking date.

**Purpose:** Daily shipment activity and delivery-performance trends.

**Used for:**
- Shipment volume trends
- Delivery-rate trends
- On-time delivery trends
- Daily delayed-delivery analysis

### 2.2 `gold_carrier_metrics`

**Grain:** One row per carrier.

**Purpose:** Measure carrier-level shipment and delivery performance.

**Used for:**
- Shipment volume by carrier
- Average delivery time
- On-time delivery rate
- Delayed deliveries
- Freight metrics

### 2.3 `gold_route_metrics`

**Grain:** One row per route.

**Purpose:** Measure route-level delivery performance and identify routes with delayed deliveries.

**Used for:**
- Shipment volume by route
- Average delivery time
- On-time delivery rate
- Delayed deliveries

### 2.4 `gold_hub_metrics`

**Grain:** One row per hub.

**Purpose:** Measure shipment flow and delivery activity by hub.

**Used for:**
- Shipment volume by hub
- Hub flow analysis
- Delivery performance by hub

---

## 3. KPI Definitions

The exact columns produced by the Gold notebook are the source of truth for the implemented metrics. The following business metrics are represented in the Gold layer where applicable:

| KPI | Definition |
|---|---|
| Total shipments | Count of trusted shipment records included in the relevant aggregation |
| Delivered shipments | Shipment records with a completed delivery outcome/status according to the Gold transformation logic |
| Delayed deliveries | Shipment records classified as delayed according to the Gold transformation logic |
| Delivery rate | Delivered shipments divided by total shipments × 100 |
| On-time delivery rate | On-time delivered shipments divided by eligible delivered shipments × 100, according to the Gold transformation logic |
| Average delivery hours | Average elapsed time between the applicable shipment timestamps used by the Gold transformation |
| Total freight | Aggregated freight amount from trusted shipment records |
| Hub flow counts | Shipment/event flow counts aggregated by hub |

The Gold notebook is the authoritative source for the implemented SQL expressions and column names.

---

## 4. Validation

Before downstream reporting, validate that:

- Gold tables are created successfully.
- Gold tables read from `trusted_shipments`, not `silver_shipments` directly.
- Gold row counts are consistent with the intended aggregation grain.
- KPI percentages remain within logical 0–100% bounds.
- Aggregations do not introduce duplicate rows at their declared grain.
- Trusted-only filtering is preserved.
- Gold outputs can be consumed by the dashboard/reporting layer.

---

## 5. Verified Week 07 Outputs

The completed Week 07 implementation produced the following Gold table row counts:

| Gold table | Verified rows |
|---|---:|
| `gold_shipment_daily_metrics` | 180 |
| `gold_carrier_metrics` | 9 |
| `gold_route_metrics` | 100 |
| `gold_hub_metrics` | 13 |

These counts describe the current executed outputs and may change if the Trusted input data changes.

---

## 6. Data Flow

```text
Raw Data
   |
   v
Bronze
   |
   v
Silver
   |
   v
Week 06 DQ Evaluation
   |
   +------------------+
   |                  |
   v                  v
Trusted            Quarantine
Silver
   |
   v
Gold Aggregations
   |
   +------------------------------+
   |              |               |
   v              v               v
Daily Metrics   Carrier         Route/Hub
                Metrics         Metrics
   |
   +--------------+--------------+
                  |
                  v
             Reporting /
             Dashboard
```

---

## 7. Downstream Use

The Gold tables are intended for Week 08 reporting/dashboard work. Downstream reporting should consume these Gold outputs rather than Bronze or untrusted Silver data.

---

**Status:** Week 07 Gold metric definitions updated to match the implemented Gold layer.
