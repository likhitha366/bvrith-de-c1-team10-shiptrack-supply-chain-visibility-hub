# Power BI Dashboard

**Project:** ShipTrack — Supply Chain Visibility Hub  
**Weeks covered:** 8–9

## Dashboard Artifact

Current Power BI file:

```text
dashboard/Team10-PowerBI-Report.pbix
```

The PBIX is the Week 08 working dashboard carried into Week 09 for refinement. Do not maintain multiple heavy PBIX versions in the repository.

## Source Rule

Power BI reporting is based on the approved Gold outputs:

- `gold_shipment_daily_metrics`
- `gold_carrier_metrics`
- `gold_route_metrics`
- `gold_hub_metrics`

The dashboard should not connect directly to Raw, Bronze, Silver detail, Candidate, or Quarantine data.

## Dashboard Use

The Gold tables support:

- Overall shipment volume and delivery-performance views
- Daily shipment trends
- Carrier comparisons
- Route comparisons
- Hub-level shipment-flow analysis

One Gold table may support multiple visuals. Visuals should be organised around business questions rather than around the number of Gold tables.

## Week 08 Validation

- Gold outputs were prepared for Power BI consumption.
- The working PBIX was added under `dashboard/`.
- Gold sample/export files were added under `data_sample/gold_exports/`.
- Dashboard screenshots are stored under `screenshots/`.

## Week 09 Refinement

Week 09 focuses on refinement of the same Week 08 dashboard rather than rebuilding the report from scratch.

Checks to perform and document:

- Visual titles and labels are clear.
- KPI and number formatting is consistent.
- Slicers and filters behave as intended for their owning Gold tables.
- Important dashboard values reconcile to the corresponding Gold aggregation under the same filter scope.
- No unsafe relationship is introduced merely to force unrelated Gold tables to respond to the same slicer.
- Insights in `docs/dashboard_insights.md` are based on observable data and state any relevant limitations.

## Evidence

Dashboard evidence is stored in:

```text
screenshots/
```

Week 08 dashboard screenshots are present. Week 09-specific refinement screenshots should be added only when genuine final/refinement evidence is available.

## File-Size Rule

If the PBIX becomes too large to manage cleanly in GitHub, retain the dashboard screenshots and documentation here and record the external mentor-review location in this file. Do not repeatedly upload multiple PBIX versions.
