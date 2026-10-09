# Databricks Notebooks

Run in this order in Databricks (`workspace.default`). Notebooks 01–06 are committed with their executed outputs.

| Notebook | Week | Purpose | Main outputs |
|---|---:|---|---|
| `01_data_exploration.ipynb` | 3 | Explore and profile the raw files | exploration evidence |
| `02_bronze_ingestion.ipynb` | 4 | Load the six raw files as Bronze tables | `bronze_*` (6) |
| `03_silver_transformations.ipynb` | 5 | Build the Silver tables | `silver_*` (6) |
| `04_data_quality_checks.ipynb` | 6 | Evaluate DQ rules and route each record | `candidate_*`, `dq_*_eval`, `trusted_*`, `quarantine_*` |
| `05_gold_aggregations.ipynb` | 7 | Build Gold facts and summaries from Trusted | `gold_fact_*` (3), Gold summaries (5) |
| `06_powerbi_export.ipynb` | 8 | Register, check and export Gold for Power BI | `data_sample/gold_exports/` |
| `07_streaming_simulation.ipynb` | 10 | Auto Loader drops, stream DQ and live events | `bronze_scan_event_stream` to `gold_fact_scan_event` |
