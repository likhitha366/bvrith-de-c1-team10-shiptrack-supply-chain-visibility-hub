# Data Dictionary

**Project:** ShipTrack – Supply Chain Visibility Hub  
**Week:** 2  
**Purpose:** Define raw source files, field definitions, primary/foreign keys, Silver table mapping, and streaming event schema.

---

# 1. Source File Catalog

| File Name | Grain | Purpose | Approx. Rows | Notes |
|-----------|-------|---------|-------------:|------|
| shipments.parquet | One row per shipment | Stores shipment lifecycle and delivery details | ~5000 | Main business dataset |
| hubs.json | One row per hub | Warehouse and hub master data | ~25 | Reference dataset |
| carriers.csv | One row per carrier | Carrier information | ~15 | Reference dataset |
| routes.csv | One row per route | Route mapping between hubs | ~120 | Reference dataset |
| scan_events.csv | One row per shipment scan | Historical shipment tracking events | ~25000 | Multiple scans per shipment |
| exceptions.csv | One row per exception | Shipment exception records | ~800 | Linked with scan events |
| streaming/scan_event.json | One row per streaming event | Real-time shipment tracking events | Incremental | NDJSON streaming files |

---

# 2. Raw File Schema: shipments.parquet

| Field Name | Data Type | Required? | Example | Description |
|------------|-----------|-----------|---------|-------------|
| source_record_id | string | Yes | SRC000001 | Physical source record identifier |
| shipment_id | string | Yes | SHP10001 | Unique shipment identifier |
| order_id | string | Yes | ORD50001 | Customer order ID |
| origin_hub_id | string | Yes | HUB001 | Shipment origin hub |
| destination_hub_id | string | Yes | HUB010 | Shipment destination hub |
| carrier_id | string | Yes | CAR005 | Assigned carrier |
| route_id | string | Yes | RTE012 | Shipping route |
| service_level | string | Yes | EXPRESS | Delivery priority |
| shipment_status | string | Yes | IN_TRANSIT | Current shipment status |
| pickup_time | timestamp | Yes | 2026-07-01 10:30:00 | Pickup timestamp |
| expected_delivery_time | timestamp | Yes | 2026-07-03 18:00:00 | Expected delivery |
| actual_delivery_time | timestamp | No | 2026-07-03 17:10:00 | Actual delivery |
| delivery_outcome | string | No | DELIVERED | Final delivery status |
| run_id | string | Yes | RUN001 | Data generation run |

---

# 3. Raw File Schema: hubs.json

| Field Name | Data Type | Required? | Example | Description |
|------------|-----------|-----------|---------|-------------|
| source_record_id | string | Yes | SRC-H001 | Physical record ID |
| hub_id | string | Yes | HUB001 | Primary Hub ID |
| hub_name | string | Yes | Hyderabad Hub | Hub name |
| city | string | Yes | Hyderabad | Hub city |
| state | string | Yes | Telangana | State |
| region | string | Yes | South | Region |
| hub_type | string | Yes | Distribution Center | Hub category |
| capacity_band | string | Yes | Large | Capacity classification |
| active_status | string | Yes | Active | Hub status |

---

# 4. Raw File Schema: carriers.csv

| Field Name | Data Type | Required? | Example | Description |
|------------|-----------|-----------|---------|-------------|
| source_record_id | string | Yes | SRC-C001 | Physical record ID |
| carrier_id | string | Yes | CAR001 | Primary Carrier ID |
| carrier_name | string | Yes | BlueDart | Carrier name |
| transport_mode | string | Yes | ROAD | Transport mode |
| primary_service_level | string | Yes | EXPRESS | Default service level |
| active_status | string | Yes | Active | Carrier status |

---

# 5. Raw File Schema: routes.csv

| Field Name | Data Type | Required? | Example | Description |
|------------|-----------|-----------|---------|-------------|
| source_record_id | string | Yes | SRC-R001 | Physical record ID |
| route_id | string | Yes | RTE001 | Route ID |
| origin_hub_id | string | Yes | HUB001 | Source hub |
| destination_hub_id | string | Yes | HUB010 | Destination hub |
| service_level | string | Yes | STANDARD | Service level |
| transport_mode | string | Yes | ROAD | Transport mode |
| distance_km | double | Yes | 580 | Distance |
| expected_transit_hours | double | Yes | 12 | Transit time |
| route_band | string | Yes | Medium | Route category |
| active_status | string | Yes | Active | Route status |

---

# 6. Raw File Schema: scan_events.csv

| Field Name | Data Type | Required? | Example | Description |
|------------|-----------|-----------|---------|-------------|
| source_record_id | string | Yes | SRC-S001 | Physical record ID |
| scan_id | string | Yes | SCN0001 | Scan identifier |
| shipment_id | string | Yes | SHP10001 | Shipment reference |
| event_sequence_no | integer | Yes | 1 | Scan order |
| event_type | string | Yes | PICKUP | Scan event |
| shipment_status | string | Yes | PICKED_UP | Shipment status |
| event_time | timestamp | Yes | 2026-07-01 10:30:00 | Event timestamp |
| hub_id | string | Yes | HUB001 | Hub reference |
| carrier_id | string | Yes | CAR005 | Carrier reference |
| route_id | string | Yes | RTE012 | Route reference |
| package_condition | string | Yes | GOOD | Package condition |
| exception_type | string | No | Delay | Exception type |
| status_reason | string | No | Weather | Status reason |
| run_id | string | Yes | RUN001 | Generation run |

---

# 7. Raw File Schema: exceptions.csv

| Field Name | Data Type | Required? | Example | Description |
|------------|-----------|-----------|---------|-------------|
| source_record_id | string | Yes | SRC-E001 | Physical record ID |
| exception_id | string | Yes | EXC001 | Exception ID |
| shipment_id | string | Yes | SHP10001 | Shipment reference |
| scan_id | string | Yes | SCN0001 | Scan reference |
| exception_type | string | Yes | Delay | Exception category |
| exception_time | timestamp | Yes | 2026-07-02 09:30:00 | Exception timestamp |
| hub_id | string | Yes | HUB005 | Hub |
| severity | string | Yes | Major | Severity |
| resolution_status | string | Yes | Resolved | Resolution |
| resolution_time | timestamp | No | 2026-07-02 14:00:00 | Resolution time |

---

# 8. Primary and Foreign Keys

## Primary Keys

| Table | Primary Key |
|--------|-------------|
| shipments | shipment_id |
| hubs | hub_id |
| carriers | carrier_id |
| routes | route_id |
| scan_events | scan_id |
| exceptions | exception_id |

## Foreign Keys

| Child Table | Foreign Key | Parent Table |
|-------------|-------------|--------------|
| shipments | carrier_id | carriers |
| shipments | route_id | routes |
| shipments | origin_hub_id | hubs |
| shipments | destination_hub_id | hubs |
| scan_events | shipment_id | shipments |
| scan_events | carrier_id | carriers |
| scan_events | route_id | routes |
| scan_events | hub_id | hubs |
| exceptions | shipment_id | shipments |
| exceptions | scan_id | scan_events |

---

# 9. Canonical Silver Table Design

Final Silver table name

```text
silver_candidate_shipments
```

| Silver Field | Data Type | Source Mapping | Business Meaning |
|--------------|-----------|----------------|------------------|
| shipment_id | string | shipment_id | Business shipment identifier |
| order_id | string | order_id | Customer order |
| pickup_date | date | pickup_time | Shipment pickup date |
| delivery_date | date | actual_delivery_time | Delivery date |
| carrier_name | string | carriers.carrier_name | Carrier information |
| route_id | string | route_id | Shipping route |
| service_level | string | service_level | Delivery priority |
| shipment_status | string | shipment_status | Current shipment status |
| delivery_outcome | string | delivery_outcome | Final shipment outcome |

---

# 10. Streaming Event Schema

| Field Name | Data Type | Required? | Example | Description |
|------------|-----------|-----------|---------|-------------|
| event_id | string | Yes | EVT0001 | Streaming event ID |
| shipment_id | string | Yes | SHP10001 | Shipment reference |
| event_sequence_no | integer | Yes | 5 | Event sequence |
| event_type | string | Yes | ARRIVED_AT_HUB | Event category |
| shipment_status | string | Yes | IN_TRANSIT | Shipment status |
| event_time | timestamp | Yes | 2026-07-03T10:15:00Z | Event timestamp |
| producer_time | timestamp | Yes | 2026-07-03T10:15:02Z | Producer timestamp |
| hub_id | string | Yes | HUB003 | Hub reference |
| carrier_id | string | Yes | CAR005 | Carrier reference |
| route_id | string | Yes | RTE012 | Route reference |
| origin_hub_id | string | Yes | HUB001 | Origin hub |
| destination_hub_id | string | Yes | HUB010 | Destination hub |
| service_level | string | Yes | EXPRESS | Delivery priority |
| transport_mode | string | Yes | ROAD | Transport mode |
| package_condition | string | Yes | GOOD | Package condition |
| exception_type | string | No | Delay | Exception type |
| source_system | string | Yes | ShipTrack Generator | Source application |
| schema_version | string | Yes | 1.0 | Event schema version |
| run_id | string | Yes | RUN001 | Generation run |

---
