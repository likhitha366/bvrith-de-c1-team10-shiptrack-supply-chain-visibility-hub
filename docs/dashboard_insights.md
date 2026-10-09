# Dashboard Insights — ShipTrack

**Week:** 9 | **Team:** 10 | **Report:** `dashboard/powerbi_1_2_3pages.pbit`
**Scope of every insight below:** all trusted shipments booked 1 January – 29 June 2026, no slicer applied, unless a scope is stated. Synthetic data; fictional educational analysis.

Every value is calculated from the approved Gold tables (`gold_fact_shipment`, `gold_fact_shipment_exception`, `gold_shipment_delay_summary`, `gold_shipment_status_exception_summary`) and can be reproduced from `data_sample/gold_exports/`.

---

## 1. Headline KPIs

| KPI | Value | Owning Gold table |
|---|---:|---|
| Total Shipments | 99,857 | `gold_fact_shipment` |
| Delivered Shipments | 77,929 (78.0 %) | `gold_fact_shipment` |
| On-Time Delivery Rate | 74.76 % | `gold_fact_shipment` |
| Average Delay, late deliveries only | 229.6 minutes (19,152 late deliveries) | `gold_fact_shipment` |
| Average End-to-End Transit | 32.2 hours | `gold_fact_shipment` |
| Exception Rate | 14.79 % (14,772 shipments) | `gold_fact_shipment_exception` |
| First-Attempt Delivery Success | 86.09 % | `gold_fact_shipment` |

## 2. Insights

### Insight 1 — Priority shipments miss their promise most often

| Field | Content |
|---|---|
| Question | Does a higher service level deliver more reliably? |
| Observation | On-time rate is 92.7 % for STANDARD (37,906 shipments), 77.1 % for EXPRESS (41,027) and 37.7 % for PRIORITY (20,924). PRIORITY is also the fastest: average transit 27.9 h against 34.8 h for STANDARD. |
| Page / visual | Performance — delay band by service level; Overview — service-level slicer with the on-time card |
| Owning Gold | `gold_fact_shipment` (`service_level`, `on_time_flag`, `transit_hours`) |
| Interpretation | PRIORITY shipments are moved faster but are judged against a tighter promise, so they are late more often. |
| Limitation | This is a hypothesis about promise windows. Gold does not store how each promise was set. |

### Insight 2 — Two carriers are about ten points below the rest

| Field | Content |
|---|---|
| Question | Which carriers need attention? |
| Observation | C008 HarborLink Cargo (65.2 %) and C004 DeltaLine Transport (66.8 %) have the lowest on-time rates. The other seven carriers are between 75.6 % and 77.2 %. |
| Page / visual | Performance — carrier table |
| Owning Gold | `gold_fact_shipment` joined to `gold_dim_carrier`; summary in `gold_carrier_performance_summary` |
| Interpretation | Both carriers are the RAIL carriers; RAIL as a mode is at 66.0 % on time against about 76.4 % for ROAD and AIR. The gap follows the mode, not one company. |
| Limitation | Carrier and mode cannot be separated with the current data because each carrier has one mode. |

### Insight 3 — Reliability depends strongly on where the shipment starts

| Field | Content |
|---|---|
| Question | Is performance even across regions? |
| Observation | On-time rate by origin region: North 82.9 %, South 76.1 %, West 75.0 %, East 66.1 %, Central 60.5 %. Central also has the longest average transit (38.1 h). |
| Page / visual | Overview — status by region; region slicer with the on-time card |
| Owning Gold | `gold_fact_shipment[origin_hub_id]` → `gold_dim_hub[region]` |
| Interpretation | Central and East origins are the weakest part of the network. |
| Limitation | Region is the origin hub's region only; destination effects are not separated. |

### Insight 4 — Route performance is extreme, not gradual

| Field | Content |
|---|---|
| Question | Are late deliveries spread across routes or concentrated? |
| Observation | Some routes with about 1,000 shipments are almost always on time (R031 100 %, R030 99.9 %, R055 99.9 %) while others are never on time (R027, R096, R047, R028 and R083 are all at 0 %). |
| Page / visual | Performance — route volume vs on-time rate |
| Owning Gold | `gold_route_reliability_summary`, `gold_fact_shipment` |
| Interpretation | A 0 % route points to a promise that the lane cannot meet (expected transit hours set too low), not to day-to-day operations. These lanes should be reviewed first. |
| Limitation | Hypothesis only. The data is synthetic and the promise-setting rule is not in Gold. |

### Insight 5 — One late delivery in three is more than four hours late

| Field | Content |
|---|---|
| Question | When we are late, how late? |
| Observation | Of 77,929 delivered shipments: 75.4 % on time, 7.9 % late by 1–60 minutes, 8.3 % late by 61–240 minutes and 8.4 % late by more than 240 minutes. |
| Page / visual | Performance — delay band column chart |
| Owning Gold | `gold_shipment_delay_summary` (`delay_band`, `shipment_count`) |
| Interpretation | Lateness is not mostly small slips; the three late bands are almost equal in size. |
| Limitation | This table is on a **delivery-date** basis. Its on-time share (75.4 %) is not the same measure as the KPI card (74.76 %), which excludes shipments without a valid promise. |

### Insight 6 — Address issues are the largest exception type

| Field | Content |
|---|---|
| Question | What kind of exception happens most? |
| Observation | 18,306 exception occurrences on 14,772 shipments. ADDRESS_ISSUE is 5,643 (30.8 %); the other six types are each between 2,072 and 2,173. 5,604 exceptions (30.6 %) are still OPEN and 5,053 are HIGH severity. |
| Page / visual | Exceptions + Live — exception type column chart and severity card |
| Owning Gold | `gold_fact_shipment_exception` |
| Interpretation | Address validation at booking is the single change with the largest possible effect on exception volume. |
| Limitation | Exception rate is nearly flat across carriers (14.4–15.1 %), so exceptions do not explain the carrier on-time gap. |

### Insight 7 — Volume and reliability are stable month to month

| Field | Content |
|---|---|
| Question | Is there a trend over the six months? |
| Observation | Monthly bookings stay between 15,514 (February) and 17,277 (March). Monthly on-time rate stays between 74.4 % and 75.3 %. |
| Page / visual | Overview — shipments over time; month slicer |
| Owning Gold | `gold_fact_shipment[booking_date]` → `gold_dim_date` |
| Interpretation | There is no seasonal effect in this period. The differences that matter are by service level, mode, region and route. |
| Limitation | Only six months of bookings are available. |

### Insight 8 — The whole open backlog is older than two weeks

| Field | Content |
|---|---|
| Question | What is still open? |
| Observation | 15,858 shipments are not delivered, returned or cancelled (IN_TRANSIT 6,906, AT_HUB 4,954, OUT_FOR_DELIVERY 3,998). All of them are in the `15_PLUS_DAYS` ageing band. |
| Page / visual | Exceptions + Live — status × ageing × exception table |
| Owning Gold | `gold_shipment_status_exception_summary` (snapshot 29 September 2026) |
| Interpretation | No conclusion about operations should be drawn from the ageing band. |
| Limitation | The source data ends on 29 June 2026 and the snapshot was taken three months later, so every open shipment is automatically older than 15 days. Ageing only becomes meaningful with a snapshot taken close to the data end date. |

## 3. Filtered reconciliation example

| Filter state | Measure | Gold value |
|---|---|---:|
| `carrier_id = 'C002'`, booking month 2026-06 | Total Shipments | 2,242 |
| same | On-Time Delivery Rate | 76.28 % (1,720 eligible delivered) |

The same slice is used in `notebooks/06_powerbi_export.ipynb` section 11.

## 4. What the dashboard cannot show

- Causes of delay. Gold has outcomes and exception types, not root causes.
- Cost or revenue impact. Freight amount is in Gold but no cost-of-delay field exists.
- Customer-level effects. There is no customer dimension.
- Live status. The report is batch; the Week-10 stream is a separate table.
