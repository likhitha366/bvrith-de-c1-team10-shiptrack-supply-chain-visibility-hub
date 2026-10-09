# Week 10 Log — Streaming Simulation and Live Scan Events

**Week:** 10  
**Date range:** 29 September – 5 October 2026  
**Team:** Team 10  
**Project:** ShipTrack: Supply Chain Visibility Hub  

---

## 1. Sprint Goal

Demonstrate ShipTrack scan events arriving over time using incremental JSON file ingestion and live scan-event processing. Validate event quality, handle malformed and duplicate events, use checkpointing and watermarking, reconcile the output, and test that rerunning the pipeline without new files does not add duplicate records.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Prepare the five approved streaming input files | B. Likhitha | Completed as recorded in the project log | `data_sample/streaming/` |
| Define the ShipTrack event schema | G. Shivani | Completed | `streaming/kafka_event_schema.json` |
| Document the streaming design | G. Shivani | Completed | `streaming/structured_streaming_design.md` |
| Configure the Databricks streaming input and event schema | G. Shivani | Implemented in notebook | `screenshots/week10_streaming_configuration.png` |
| Inspect quarantined records | G. Shivani | Evidence captured | `screenshots/week10_quarantine_results.png` |
| Inspect checkpoint and output state | G. Shivani | Evidence captured; recovery behaviour requires verification | `screenshots/week10_checkpoint_recovery.png` |
| Test rerunning without new files | G. Shivani | Test evidence prepared; verify the final result | `screenshots/week10_no_new_files_test.png` |
| Inspect controlled arrivals | G. Shivani | Evidence captured | `screenshots/week10_controlled_arrivals.png` |
| Validate final output records | G. Shivani | Basic validation evidence captured | `screenshots/week10_final_validation.png` |
| Validate all five drops and reconcile per file | Team 10 | Further verification required | Databricks notebook |
| Run and verify the continuous pipeline | Team 10 | Pending verification | Databricks pipeline and notebook |

---

## 3. Key Decisions

- File-based ingestion and live event processing demonstrate two different streaming patterns.
- The event schema defines the expected structure of incoming scan events.
- The pipeline uses `event_id` as the event deduplication key.
- A 24-hour watermark is used to manage late-arriving events.
- Checkpointing supports tracking streaming progress across restarts.
- The `availableNow` trigger is used for bounded incremental processing in Databricks.
- Kafka is documented as a design option only; no Kafka broker or topic is claimed to have been created.
- Quarantined records must be inspected separately from trusted records.
- A no-new-files test must demonstrate that rerunning the stream does not introduce additional records.

---

## 4. Blockers and Risks

| Blocker or risk | Impact | Action |
|---|---|---|
| Input files share the same filename | Files may overwrite one another if copied into a single directory without renaming | Preserve the approved source files and use the notebook's source-seeding logic |
| Week-6 reference tables use different naming conventions | Reference-table lookups may fail | Confirm the actual table names in Databricks |
| Continuous processing requires the correct pipeline mode | A triggered pipeline may not continuously process new events | Verify the pipeline configuration and serverless compute settings |
| Some streaming results have not been fully reconciled | Final completeness cannot yet be confirmed | Run the reconciliation checks and record actual results |
| A missing event was manually added to the output during troubleshooting | The output count alone does not prove that ingestion processed every event correctly | Investigate the missing event and verify the pipeline's automatic processing behaviour |

---

## 5. Evidence Added to GitHub

The following evidence screenshots have been prepared:

- `screenshots/week10_streaming_configuration.png`
- `screenshots/week10_quarantine_results.png`
- `screenshots/week10_checkpoint_recovery.png`
- `screenshots/week10_no_new_files_test.png`
- `screenshots/week10_controlled_arrivals.png`
- `screenshots/week10_final_validation.png`

Other project files:

- `notebooks/07_streaming_simulation.ipynb`
- `streaming/structured_streaming_design.md`
- `streaming/kafka_event_schema.json`
- `data_sample/streaming/`
- `weekly_logs/week10_log.md`

---

## 6. Recorded Databricks Results

The following values were observed during earlier troubleshooting. They must be reconfirmed against the final Databricks output.

| Check | Previously observed result | Verification status |
|---|---:|---|
| Controlled-arrivals records | 67 | Reconfirm against the final output |
| Unique event IDs | 67 | Reconfirm against the final output |
| Duplicate event IDs | 0 | Reconfirm against the final output |
| Quarantine records | 2 | Inspect the final quarantine output |
| No-new-files rerun | 67 records before and after was the expected result | Confirm actual rerun output |
| Five-drop reconciliation | Not fully established | Pending |
| Continuous pipeline count growth | Not established | Pending |
| Producer stop and restart | Not established | Pending |

**Important:** The controlled-arrivals output previously required a manual correction for event `EVT000039`. Therefore, the output count must not be treated as proof that all five drops were automatically processed correctly.

---

## 7. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI assisted with drafting the streaming notebook, event schema, streaming design, and explanations of Auto Loader, checkpoints, and watermarks. |
| What we changed after AI suggestions | Workspace paths, table names, and configuration were checked during Databricks troubleshooting. Any additional changes should be documented after verification. |
| What we verified manually | Input files, streaming output, quarantine records, checkpoint state, and basic data-quality counts were inspected during troubleshooting. |
| What remains to verify | Complete five-drop reconciliation, automatic handling of the missing event, the no-new-files rerun result, and continuous-pipeline behaviour. |
| What we can explain without AI | The producer-to-landing flow, ingestion checkpoints, Bronze and Silver processing, trusted and quarantined records, event deduplication, watermarking, and output validation. |

---

## 8. Next Week Preparation

- Complete the remaining Week-10 reconciliation and streaming tests.
- Verify that all five input drops are processed correctly.
- Confirm that the no-new-files rerun adds no records.
- Verify continuous-pipeline count growth and stop/restart behaviour.
- Carry the verified results and screenshots into the Week-11 pipeline walkthrough.
- Update `README.md`, `docs/pipeline_walkthrough.md`, and `docs/references.md` during Week 11.
