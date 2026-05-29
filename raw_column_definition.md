# Raw CSV Column Definitions - TaiwanLifeInsurance

## raw_life_insurance_statistics_2020_2026.csv (Taiwan Life Insurance Statistics)

**Source:** `data/raw_life_insurance_statistics_2020_2026.csv`
**Data Source:** Life Insurance Association of the R.O.C. (via fetcher script)
**Update Frequency:** Quarterly automated updates
**Extraction Strategy:** Scrape life insurance statistics from official tables.

### Columns

| Column | Type | Description | Source Field | Notes |
|---|---|---|---|---|
| `年度` | integer | Year (ROC or Gregorian based on source) | System |  |
| `季度` | string | Quarter | System | e.g., `Q1`, `Q2` |
| `項目` | string | Statistic item name | Scraped | e.g., `總保費收入` |
| `數值` | float | Statistic value | Scraped |  |
| `備註` | string | Notes | Scraped |  |
| `download_timestamp` | datetime | Data retrieval timestamp | System | `YYYY-MM-DD HH:MM:SS` |
| `process_timestamp` | datetime | CSV generation timestamp | System | `YYYY-MM-DD HH:MM:SS` |
