# Power BI Dashboard — ShipTrack

**Team:** 10 | **Weeks:** 8–9 | **File:** `dashboard/powerbi_1_2_3pages.pbit`
**Upstream:** `notebooks/05_gold_aggregations.ipynb` → `notebooks/06_powerbi_export.ipynb`

## 0. Dashboard file

`dashboard/powerbi_1_2_3pages.pbit` is a Power BI template: it holds the model (14 Gold tables, 18 relationships) and the three report pages, but no data. Open it in Power BI Desktop and sign in to the Databricks SQL warehouse; the tables then load from `workspace.default`. A data-loaded `.pbix` is not committed to this repository. The first Week 8 draft (`Team10-PowerBI-Report.pbix`) was removed on 30 September when the template replaced it.

## 1. Purpose

A three-page, Gold-only report on shipment volume, delivery reliability, hub and route performance, and exceptions. All figures are fictional educational analysis on synthetic data.

## 2. Gold source register

Power BI reads **approved Gold tables only** from Databricks (`workspace.default`) through the Databricks connector. No Raw, Bronze, Silver Candidate, Trusted Silver detail or Quarantine table is connected.

| Gold table (= Power BI table name) | Grain | Used for |
|---|---|---|
| `gold_fact_shipment` | one trusted shipment | volume, delivery, on-time, transit, backlog |
| `gold_fact_shipment_scan` | one trusted historical scan | milestone timeline on page 3 |
| `gold_fact_shipment_exception` | one exception occurrence | exception counts and severity |
| `gold_shipment_delay_summary` | delivery date × route × carrier × service level × delay band | delay-band analysis |
| `gold_carrier_performance_summary` | delivery date × carrier × service level | carrier comparison |
| `gold_route_reliability_summary` | delivery date × route × service level | route reliability |
| `gold_hub_throughput_summary` | event date × time band × hub | hub throughput and dwell |
| `gold_shipment_status_exception_summary` | snapshot date × status × ageing band × exception type | open backlog and ageing |
| `gold_dim_date`, `gold_dim_hub`, `gold_dim_carrier`, `gold_dim_route`, `gold_dim_service_level`, `gold_dim_status` | one row per member | slicers and labels |

`gold_fact_scan_event` (Week 10 streaming) is not in the report.

## 3. Relationships

All are many-to-one with single cross-filter direction (dimension filters fact). Summary and fact tables are **not** joined to each other, except exception → shipment.

| From (many) | To (one) | Active |
|---|---|---|
| `gold_fact_shipment[carrier_id]` | `gold_dim_carrier[carrier_id]` | Yes |
| `gold_fact_shipment[service_level]` | `gold_dim_service_level[service_level]` | Yes |
| `gold_fact_shipment[route_id]` | `gold_dim_route[route_id]` | No |
| `gold_fact_shipment_exception[shipment_id]` | `gold_fact_shipment[shipment_id]` | Yes |
| `gold_fact_shipment_exception[hub_id]` | `gold_dim_hub[hub_id]` | Yes |
| `gold_fact_shipment_scan[shipment_id]` | `gold_fact_shipment[shipment_id]` | No |
| `gold_fact_shipment_scan[hub_id]` | `gold_dim_hub[hub_id]` | Yes |
| `gold_fact_shipment_scan[carrier_id]` | `gold_dim_carrier[carrier_id]` | Yes |
| `gold_fact_shipment_scan[route_id]` | `gold_dim_route[route_id]` | Yes |
| `gold_carrier_performance_summary[carrier_id]` | `gold_dim_carrier[carrier_id]` | Yes |
| `gold_carrier_performance_summary[service_level]` | `gold_dim_service_level[service_level]` | Yes |
| `gold_route_reliability_summary[route_id]` | `gold_dim_route[route_id]` | No |
| `gold_route_reliability_summary[service_level]` | `gold_dim_service_level[service_level]` | Yes |
| `gold_shipment_delay_summary[carrier_id]` | `gold_dim_carrier[carrier_id]` | Yes |
| `gold_shipment_delay_summary[route_id]` | `gold_dim_route[route_id]` | No |
| `gold_shipment_delay_summary[service_level]` | `gold_dim_service_level[service_level]` | Yes |
| `gold_hub_throughput_summary[hub_id]` | `gold_dim_hub[hub_id]` | Yes |
| `gold_dim_route[service_level]` | `gold_dim_service_level[service_level]` | Yes |

Route relationships on shipment, delay and reliability tables are inactive to avoid an ambiguous path through `gold_dim_route → gold_dim_service_level`.

## 4. Page register

| Page | Business question | Main visuals | Gold sources |
|---|---|---|---|
| **Overview** | What is happening across the network? | KPI cards (total shipments, delivered, on-time rate, average transit hours, exceptions, delay band); shipments over time (line); status by region (column); route transit (bar); shipment detail table | `gold_fact_shipment`, `gold_carrier_performance_summary`, `gold_shipment_delay_summary`, `gold_dim_route`, `gold_dim_hub` |
| **Performance** | Which carriers, routes and hubs perform well or badly? | route volume vs on-time rate (combo); hub volume vs dwell (combo); delay band by service level (column); carrier table; KPI cards | `gold_route_reliability_summary`, `gold_hub_throughput_summary`, `gold_carrier_performance_summary`, `gold_shipment_delay_summary` |
| **Exceptions + Live** | Where are exceptions and what is still open? | exception type (column); status × ageing × exception table; scan milestone table; KPI cards | `gold_shipment_status_exception_summary`, `gold_fact_shipment_exception`, `gold_fact_shipment_scan`, `gold_fact_shipment` |

Each page has a page navigator.

## 5. Slicers and interaction

| Page | Slicers | Affects |
|---|---|---|
| Overview | status, service level, month, hub region, carrier, route | visuals whose table has an active relationship to the slicer's table; a slicer on a summary-table column filters that summary table only |
| Performance | carrier, service level, route, event date, status/mode, hub | each slicer filters visuals from its own Gold table and from tables related through a shared dimension |
| Exceptions + Live | delivery date, exception hub, route, carrier, status/mode, service level | same rule |

A slicer does not need to change every visual. Independent Gold summaries stay independent.

## 6. Measures

KPI definitions are in `docs/gold_metrics_definition.md` section 4. The DAX for each measure is listed in `notebooks/06_powerbi_export.ipynb` section 10c. Rates must be calculated from `gold_fact_shipment` (numerator ÷ denominator), not by averaging the `*_rate_pct` columns of a summary table.

## 7. Refresh

1. Rerun `notebooks/05_gold_aggregations.ipynb` only if Trusted Silver changed.
2. Open the PBIX in Power BI Desktop and select **Refresh** (Databricks SQL warehouse must be running).
3. Recheck the reconciliation values in section 8.

## 8. Reconciliation — Gold values with no slicer applied

Calculated from `gold_fact_shipment` / `gold_fact_shipment_exception` (Week-7 KPI contract; same rows as `data_sample/gold_exports/`).

| KPI | Gold value |
|---|---:|
| Total Shipments | 99,857 |
| Delivered Shipments | 77,929 |
| On-Time Delivery Rate | 74.76 % |
| Average End-to-End Transit Hours | 32.22 |
| Exception Rate | 14.79 % |
| First-Attempt Delivery Success Rate | 86.09 % |
| Open shipments (not delivered, returned or cancelled) | 15,858 |

Filtered check used in `notebooks/06_powerbi_export.ipynb` section 11: `carrier_id = 'C002'` and booking month `2026-06` → 2,242 shipments, on-time rate 76.28 %.

Pass condition: the Power BI card shows the same value under the same filter state.

## 9. Evidence

`screenshots/week08_*` (Gold connection, first draft, export-notebook checks) and `screenshots/week09_*` (the three refined pages; the Overview capture has slicers applied). A filtered-reconciliation screenshot is not in the repo yet.

## 10. Known limitations

- The report cannot explain *why* a route or carrier is late; Gold has no cause field beyond exception type.
- `gold_shipment_status_exception_summary` is a snapshot; ageing depends on the Gold run date.
- Booking-date visuals and delivery-date visuals are not like-for-like; titles state the date basis.
- Week 10 streaming adds `gold_fact_scan_event` as a separate governed branch; this batch report is unchanged.
