# Week 06 — DQ Rule Mapping

**Project:** ShipTrack – Supply Chain Visibility Hub  
**Week:** 6

This document maps the shipment data-quality rules to the Silver columns and reference tables used by the Week 6 DQ framework.

| Rule ID | Rule Name | Columns Used | Other Tables | What It Checks |
|---|---|---|---|---|
| DQ-SHP-001 | Shipment identity | `source_record_id`, `shipment_id`, `order_reference` | None | Required identity fields are present and shipment identity is valid. |
| DQ-REF-001 | Reference integrity | `origin_hub_id`, `destination_hub_id`, `carrier_id`, `route_id` | `silver_hubs`, `silver_carriers`, `silver_routes` | Referenced hub, carrier, and route IDs exist. |
| DQ-TIM-001 | Chronology | `booking_ts`, `pickup_ts`, `promised_delivery_ts`, `actual_delivery_ts`, `return_completed_ts` | None | Shipment timestamps follow the defined chronological relationships. |
| DQ-SCN-001 | Scan sequence | `shipment_id` / scan `reference_id` | `silver_scan_events` | Linked scan events have valid sequence numbers, start at sequence 1, contain no sequence gaps, and have timestamps increasing with sequence. |
| DQ-RTE-001 | Route consistency | `route_id`, `origin_hub_id`, `destination_hub_id`, `service_level`, `transport_mode`, `booking_ts` | `silver_routes` | Shipment route hubs and route attributes agree, and the route is active/effective for the booking date. |
| DQ-DEL-001 | Delivery/status consistency | `latest_status`, `delivery_outcome`, `actual_delivery_ts`, `return_completed_ts` | None | Delivery and status fields are logically consistent. |
| DQ-MEA-001 | Measures | `package_weight_kg`, `package_count`, `freight_amount_inr`, `attempt_count` | None | Shipment measures are valid and within the expected non-negative/required ranges. |
| DQ-EVT-001 | Event/schema | Required identity, timestamp, status, and enum fields | None | Required fields are present and controlled values are valid. |

## Notes

- The Week 6 framework keeps one quarantine row per `source_record_id`.
- `failed_rule_ids` stores all failed rule IDs for a record as an array.
- `failure_details` stores the corresponding failure explanations.
- `DQ-SCN-001` does not enforce a fixed `event_type` progression because the available event types do not define a strict linear business sequence in the current schema.
- This mapping describes the implemented shipment DQ framework; execution evidence and final counts are captured separately in the Databricks notebook/screenshots.
