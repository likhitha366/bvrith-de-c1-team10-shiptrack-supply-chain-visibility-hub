# Dashboard Insights

**Project:** ShipTrack — Supply Chain Visibility Hub  
**Reporting stage:** Week 09  
**Source:** Approved Gold outputs used by the Week 08 Power BI dashboard and carried into Week 09 refinement

---

## 1. Dashboard Scope

The dashboard uses the following Gold tables:

- `gold_shipment_daily_metrics` — daily shipment and delivery-performance trends
- `gold_carrier_metrics` — carrier-level shipment and delivery performance
- `gold_route_metrics` — route-level shipment and delivery performance
- `gold_hub_metrics` — hub-level shipment flow and delivery performance

The dashboard is intended to communicate shipment volume, delivery performance and operational comparisons without bypassing the Gold layer.

## 2. Evidence-Backed Observations

### 1. Daily shipment activity is available for trend analysis

The daily Gold table contains **180 verified rows**, representing the current booking-date aggregation used for daily reporting. This supports a time-based shipment-volume view in Power BI.

**Owning Gold table:** `gold_shipment_daily_metrics`  
**Evidence:** Week 07 verified Gold output count

### 2. Carrier-level comparison is supported by a compact summary

`gold_carrier_metrics` contains **9 verified carrier rows**. This supports carrier-level comparison of the shipment and delivery metrics implemented in the Gold layer.

**Owning Gold table:** `gold_carrier_metrics`  
**Evidence:** Week 07 verified Gold output count

### 3. Route-level operational comparison is supported

`gold_route_metrics` contains **100 verified route rows**. The table supports route-level shipment-volume and delivery-performance analysis in the dashboard.

**Owning Gold table:** `gold_route_metrics`  
**Evidence:** Week 07 verified Gold output count

### 4. Hub-level shipment flow can be compared

`gold_hub_metrics` contains **13 verified hub rows**, supporting hub-level shipment-flow and delivery-performance views.

**Owning Gold table:** `gold_hub_metrics`  
**Evidence:** Week 07 verified Gold output count

### 5. The Gold layer provides different reporting grains

The four Gold tables represent different grains: booking date, carrier, route and hub. They should therefore be used for the questions each table was designed to answer rather than being treated as one interchangeable dataset.

### 6. Dashboard metrics should be reconciled to their owning Gold table

A Power BI value should be considered validated only when the equivalent Gold aggregation agrees under the same filter scope. This is particularly important when visuals from different Gold tables appear on the same dashboard page.

## 3. Business Interpretation

The current dashboard structure supports three broad questions:

1. **How much shipment activity is occurring over time?** — daily Gold metrics.
2. **How does delivery performance vary across operational dimensions?** — carrier, route and hub Gold summaries.
3. **Can the reported dashboard values be traced back to governed data?** — reconciliation to the owning Gold table.

These observations describe what the available Gold data can support. They do not establish causal reasons for delays, route performance or carrier performance without additional approved data.

## 4. Dashboard-to-Gold Mapping

| Dashboard Analysis | Gold Table | Main Reporting Use |
|---|---|---|
| Daily shipment trend | `gold_shipment_daily_metrics` | Shipment volume and delivery trends |
| Carrier comparison | `gold_carrier_metrics` | Carrier performance comparison |
| Route comparison | `gold_route_metrics` | Route performance comparison |
| Hub comparison | `gold_hub_metrics` | Hub flow and performance comparison |

## 5. Week 09 Validation Checklist

- [x] Dashboard reporting remains based on approved Gold outputs.
- [x] Gold table grains are documented.
- [x] Verified Gold row counts are recorded.
- [x] Dashboard-to-Gold ownership is documented.
- [x] Every final dashboard KPI has a recorded same-filter reconciliation result.
- [x] Week 09 refinement screenshots are added when genuine final evidence is available.

## 6. Limitations

- The Gold row counts describe the current executed dataset and may change when upstream Trusted data changes.
- GitHub cannot inspect the internal PBIX visual configuration as ordinary Markdown/source content.
- The current Gold summaries support descriptive analysis; they should not be used to claim operational causation that is not represented in the Gold data.

**Status:** Dashboard insight documentation updated through Week 09 without inventing dashboard values or unsupported causal conclusions.
