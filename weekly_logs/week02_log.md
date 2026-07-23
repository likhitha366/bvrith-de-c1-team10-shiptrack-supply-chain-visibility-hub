# Week 02 Log — Meet the Data: Contracts, Grains and Checksums

**Week:** 2  
**Date Range:** 21 July 2026 – 27 July 2026  
**Team:** Team 10  
**Project:** ShipTrack – Supply Chain Visibility Hub

---

# 1. Sprint Goal

The objective for Week 02 was to understand the ShipTrack dataset by identifying all raw and reference source files, documenting their schemas, defining primary and foreign keys, understanding the business grain of each dataset, documenting synthetic data assumptions, and preparing sample datasets before implementing the Bronze layer.

---

# 2. Work Completed

| Task | Owner | Status | Evidence |
|------|-------|--------|----------|
| Reviewed ShipTrack Project Playbook | Team 10 | ✅ Completed | Project Playbook PDF |
| Explored all source datasets | Team 10 | ✅ Completed | Dataset Pack |
| Identified all raw and reference files | Team 10 | ✅ Completed | docs/data_dictionary.md |
| Documented source file catalog | Team 10 | ✅ Completed | docs/data_dictionary.md |
| Documented field names, data types and descriptions | Team 10 | ✅ Completed | docs/data_dictionary.md |
| Defined Primary Keys and Foreign Keys | Team 10 | ✅ Completed | docs/data_dictionary.md |
| Designed Canonical Silver table mapping | Team 10 | ✅ Completed | docs/data_dictionary.md |
| Documented Streaming Event Schema | Team 10 | ✅ Completed | docs/data_dictionary.md |
| Documented Synthetic Data Assumptions | Team 10 | ✅ Completed | docs/synthetic_data_assumptions.md |
| Prepared raw sample datasets | Team 10 | ✅ Completed | data_sample/raw/ |
| Verified dataset relationships and business grain | Team 10 | ✅ Completed | Project Documentation |
| Updated Week 02 documentation | Team 10 | ✅ Completed | GitHub Repository |

---

# 3. Key Decisions

- Used the official ShipTrack project dataset provided in the Data Pack.
- Preserved the original business grain for all datasets.
- Documented all raw, reference, and streaming datasets before data ingestion.
- Defined Primary Keys and Foreign Keys to maintain referential integrity.
- Created a canonical Silver table design for future transformations.
- Used only synthetic logistics data provided for educational purposes.
- Followed the official project folder structure and GitHub naming conventions.

---

# 4. Blockers / Risks

| Blocker | Impact | Resolution |
|----------|--------|------------|
| Understanding relationships between shipment, scan events and exceptions | Medium | Studied project documentation and data contracts |
| Identifying Primary and Foreign Keys | Low | Cross-verified relationships across datasets |
| Understanding streaming event structure | Low | Reviewed streaming dataset and project playbook |
| Mapping raw fields to Silver schema | Low | Designed canonical Silver table mapping |

---

# 5. Validation Performed

- Verified all source files are present in the dataset.
- Verified field names and data types.
- Verified primary and foreign key relationships.
- Verified business grain for each dataset.
- Verified sample datasets match original source structure.
- Reviewed streaming event schema.
- Ensured documentation follows the project template.

---

# 6. Evidence Added to GitHub

```
docs/
├── data_dictionary.md
└── synthetic_data_assumptions.md

data_sample/
└── raw/
    ├── shipments_sample.parquet
    ├── hubs_sample.json
    ├── carriers_sample.csv
    ├── routes_sample.csv
    ├── scan_events_sample.csv
    └── exceptions_sample.csv

weekly_logs/
└── week02_log.md
```

---

# 7. AI Transparency Note

| Question | Response |
|----------|----------|
| Where AI helped | Assisted in preparing the Data Dictionary, Synthetic Data Assumptions, Canonical Silver mapping, and Week 02 documentation based on project requirements. |
| What we changed after AI suggestion | Verified field names, dataset relationships, keys, and documentation against the official ShipTrack dataset and updated the content accordingly. |
| What we verified manually | Source files, schema, field names, business grain, primary keys, foreign keys, streaming event structure, and dataset relationships. |
| What we can explain without AI | Project overview, dataset structure, source files, business grain, schema, dataset relationships, and Week 02 documentation. |

---

# 8. Next Week Preparation

- Begin Bronze layer implementation.
- Load all raw source files into Bronze tables.
- Preserve raw data without transformations.
- Add ingestion metadata (`source_file`, `ingestion_ts`, `run_id`, `source_record_id`).
- Validate source-to-Bronze reconciliation.
- Implement data quality checks.
- Update Bronze ingestion notebooks.
- Commit Bronze layer implementation to GitHub.

---

# 9. Week 02 Summary

✅ Completed documentation of all source datasets.

✅ Documented schemas, keys, and relationships.

✅ Prepared sample raw datasets.

✅ Created Data Dictionary.

✅ Documented Synthetic Data Assumptions.

✅ Designed Canonical Silver schema.

✅ Prepared Week 02 GitHub documentation.

**Week 02 Status:** ✅ Completed Successfully
