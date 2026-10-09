# Pipeline Walkthrough

**Week:** 11  
**Purpose:** Explain the full end-to-end project flow.

---

## 1. Pipeline Run Order

| Step | Notebook / File | Reads | Output |
|---:|---|---|---|
| 1 | Upload the six raw files to `/Volumes/ship_track/default/ship_track_volume/` | source files | `shipments.parquet`, `scan_events.csv`, `exceptions.csv`, `routes.csv`, `carriers.csv`, `hubs.json` |
| 2 | `notebooks/01_data_exploration.ipynb` | raw files | exploration and profiling evidence |
| 3 | `notebooks/02_bronze_ingestion.ipynb` | raw files | `bronze_*` (6 tables), raw-to-Bronze count check |
| 4 | `notebooks/03_silver_transformations.ipynb` | `bronze_*` | `silver_*` (6 tables) |
| 5 | `notebooks/04_data_quality_checks.ipynb` | `silver_*` | `candidate_*`, `dq_*_eval`, `trusted_*`, `quarantine_*` |
| 6 | `notebooks/05_gold_aggregations.ipynb` | `trusted_shipments`, `trusted_scan_events`, `trusted_exceptions` | 3 Gold facts and 5 Gold summaries |
| 7 | `notebooks/06_powerbi_export.ipynb` | Gold facts, summaries, dimensions | grain and relationship checks, `data_sample/gold_exports/` |
| 8 | `dashboard/powerbi_1_2_3pages.pbit` | Gold tables through the Databricks connector | three-page Power BI report |
| 9 | `notebooks/07_streaming_simulation.ipynb` | five NDJSON drops, `trusted_*` references | `bronze_scan_event_stream` to `gold_fact_scan_event`, live Bronze |

---

## 2. Architecture Explanation

Raw Sources → Bronze → Silver → Data Quality → Gold → Power BI → Streaming Simulation

Six raw files (one Parquet, four CSV, one JSON) are loaded as they are into six Bronze tables, with the source file name kept on every row and raw and Bronze counts compared.
Silver builds one table per Bronze table: scan events are renamed and typed, and the other five tables are de-duplicated.
The data-quality notebook does not change Silver. It snapshots each Silver table as a candidate table, evaluates every rule on every record, and routes the record once: to `trusted_*` if it passes all rules, or to `quarantine_*` with every failed rule and reason if it does not. Candidate always equals Trusted plus Quarantine.
Gold reads only the Trusted tables. It builds three facts (shipment, shipment scan, shipment exception) and five summaries (delay, carrier performance, route reliability, hub throughput, status and exception), each with a declared grain that is checked for duplicates.
The export notebook registers the Gold tables and six dimensions, proves the grain and relationship contract, and writes reproducible CSV exports with a manifest.
Power BI reads the Gold tables only, through the Databricks connector, into a three-page report: Overview, Performance, Exceptions + Live.
The streaming notebook is a separate branch. Auto Loader ingests five controlled scan-event drops one file at a time with a checkpoint; the events are validated against the Trusted reference tables, a 24-hour watermark and five rules, and routed to a streaming Trusted or Quarantine table and then to `gold_fact_scan_event`. A small producer and a continuous SQL pipeline show live events arriving in Bronze.

The table-level lineage is in `docs/gold_metrics_definition.md` (Gold) and `streaming/structured_streaming_design.md` (stream).

---

## 3. Known Limitations

- All data is synthetic and for education only; no figure describes a real company.
- The Week 10 streaming notebook is committed without executed outputs. Its Databricks run, the `week10_*` screenshots and the results table in `weekly_logs/week10_log.md` are still pending.
- In Silver, only scan events are renamed and typed. The other five Silver tables are de-duplicated copies of Bronze and keep the Bronze column types.
- The exceptions data-quality run does not reconcile yet (Trusted 18,330 + Quarantine 24 against 18,352 candidates). The join was corrected in the notebook; the cell has to be rerun and `docs/data_quality_summary.md` updated.
- Some Power BI KPI cards use a default sum on rate columns. The governed KPI values are the ones in `dashboard/README.md` section 8, calculated from Gold.
- The repository holds a Power BI template (`.pbit`) without data, and no screenshot of a Power BI card reconciled to Gold under a filter.
- `gold_shipment_status_exception_summary` is a snapshot taken three months after the data ends, so every open shipment falls in the oldest ageing band.
- Kafka is design only. Streaming uses file drops with Auto Loader and the `availableNow` trigger, because Databricks Free Edition runs on serverless compute.
- `src/generate_synthetic_data.py` is still the starter script and does not generate the ShipTrack files that the notebooks load.

---

## 4. How to Reproduce

1. Clone the repository and read `README.md`, `docs/problem_charter.md` and `docs/data_dictionary.md`.
2. In Databricks, upload the six raw files to `/Volumes/ship_track/default/ship_track_volume/`. Small samples of each are in `data_sample/raw/`.
3. Run notebooks `01` to `06` in order in `workspace.default`. Each notebook prints its own counts; compare them with the saved outputs in the repository.
4. Check the reconciliation in notebook `04` (Candidate = Trusted + Quarantine) and the row counts printed by the last cell of notebook `05`.
5. Open `dashboard/powerbi_1_2_3pages.pbit` in Power BI Desktop, sign in to the Databricks SQL warehouse and compare the cards with `dashboard/README.md` section 8.
6. Run notebook `07`. Section 2 places the five drops in the volume; sections 4 to 9 land and process one drop at a time; section 22.1 prints the results table for the Week 10 log.
7. Review `screenshots/README.md` for the evidence captured each week.
