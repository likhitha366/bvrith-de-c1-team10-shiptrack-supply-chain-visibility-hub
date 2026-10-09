# Week 10 Log — Streaming Simulation and Live Scan Events

**Week:** 10  
**Date range:** 29 September – 5 October 2026  
**Team:** Team 10  
**Project:** ShipTrack: Supply Chain Visibility Hub

---

## 1. Work Completed

### Streaming Configuration
- Defined the event schema for incoming scan events.
- Configured the streaming input path.
- Parsed incoming JSON records into structured columns.
- Added basic validation conditions for event IDs, shipment IDs, timestamps, schema version, and event sequence numbers.
- Applied a 24-hour watermark.
- Configured deduplication using `event_id`.

### Quarantine Results
- Read the quarantine output stored in Delta format.
- Displayed and inspected the quarantined records.

### Checkpoint and Recovery
- Inspected the checkpoint directory.
- Read the controlled-arrivals Delta output.
- Checked the total number of records and unique event IDs.

### Controlled Arrivals
- Read the controlled-arrivals output from Delta.
- Checked the total number of records and unique event IDs.
- Displayed the event records for inspection.

### Final Validation
- Checked the total number of records.
- Checked the number of unique event IDs.
- Checked for duplicate event IDs.
- Checked for null event IDs, shipment IDs, and event timestamps.

---

## 2. Evidence Screenshots

The following screenshots were prepared for Week 10:

- `screenshots/week10_streaming_configuration.png`
- `screenshots/week10_quarantine_results.png`
- `screenshots/week10_checkpoint_recovery.png`
- `screenshots/week10_no_new_files_test.png`
- `screenshots/week10_controlled_arrivals.png`
- `screenshots/week10_final_validation.png`

---

## 3. Tools and Technologies Used

- Databricks
- Apache Spark Structured Streaming
- PySpark
- Delta Lake
- GitHub

---

## 4. Summary

During Week 10, I configured the streaming input, parsed JSON events, applied basic validation, configured watermarking and deduplication, and inspected the quarantine and controlled-arrivals outputs. I also prepared screenshots documenting the streaming configuration, checkpoint state, no-new-files test, and final validation.
