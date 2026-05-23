# Raw Data Column Definition: Life Insurance Statistics (2020 - 2026 Q1)

This dataset integrates historical quarterly surrender data and detailed performance metrics for 2026 Q1.

| Column Name | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `年度` | Integer | 民國年份 (ROC Year). 109=2020, 115=2026. | 115 |
| `季度` | String | 統計季度 (Q1, Q2, Q3, Q4). | Q1 |
| `項目` | String | 統計指標名稱 (解約金, 總保費收入, 保險給付總額, 新契約保費_FYP, 淨現金流). | 解約金 |
| `數值` | Float | 數值金額 (單位：百萬新台幣 / Unit: Million TWD). | 481500 |
| `備註` | String | 數據背景說明或來源註記. | 2026 Q1 新聞報導 |

## Data Content
1. **Historical Surrender (2020-2025):** Quarterly cumulative "解約金" (Surrender Benefits).
2. **2026 Q1 Detailed Metrics:** Matches the news report "台股誘人…引爆保單解約潮".

## Source Metadata & URLs
- **News Reference (2026/05/23):** [台股誘人…引爆保單解約潮](https://udn.com/news/story/7239/8750241)
- **Primary Source (LIA-ROC):** [壽險公會統計專區](https://www.lia-roc.org.tw/index06/statis/statis.htm)
    - *2026 Q1 PDF:* [https://www.lia-roc.org.tw/storage/uploads/6a0ad8287ebc4.pdf](https://www.lia-roc.org.tw/storage/uploads/6a0ad8287ebc4.pdf)
- **Secondary Source (TII):** [保發中心統計資料庫](https://www.tii.org.tw/tii/information/statistics/report/life/)
    - *XLS Download (Requires Session):* [https://www.tii.org.tw/opencms/export/sites/tii/statistics/life/biz_info/xls/xpivomonclml.xls](https://www.tii.org.tw/opencms/export/sites/tii/statistics/life/biz_info/xls/xpivomonclml.xls)
    - *Interactive Pivot:* [https://insdb.tii.org.tw/pivot/](https://insdb.tii.org.tw/pivot/)
- **Government Open Data:** [政府資料開放平臺 - 壽險業保費收入統計表](https://data.gov.tw/dataset/25930)

## Unit Conversion
Figures in news reported in "億" (100M) are converted to "百萬" (Million) in this CSV (e.g., 4,815億 -> 481500百萬).
