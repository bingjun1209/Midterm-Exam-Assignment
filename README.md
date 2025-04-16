# 📘 Midterm-Exam-Assignment

這次期中考作業，我研究了 `Selenium` 與 `Scrapy`，並且試著抓取亞洲大學資工系的網頁老師的姓名與研究領域。

---

## 🐍 首先使用 Selenium

我使用 Selenium 自動開啟網頁、模擬瀏覽器操作，擷取副教授的姓名與研究專長，並儲存為 CSV 或 JSON 格式。

📄 [Selenium 程式碼 ➜ 點我看](./selenium_script.py)

---

## 🕷️ 接著使用 Scrapy

使用 Scrapy 爬蟲框架自動抓取網頁中每位副教授的資料，並輸出為 csv 或 json。

📄 [Scrapy 程式碼 ➜ 點我看](./csie_professors/spiders/professors.py)

**執行方式：**

- 匯出為 JSON 格式：  
  `scrapy crawl professors -o professors.json`

- 匯出為 CSV 格式：  
  `scrapy crawl professors -o professors.csv`

- 匯出為純文字格式：  
  `scrapy crawl professors -o professors.txt`

---

### 💾 加分項目：資料儲存進 SQLite

我也將用 Scrapy 抓下來的資料進一步儲存到 SQLite 資料庫中，作為延伸應用！

- 檔案名稱：`professors.db`
- 表格內容包含教師姓名與研究專長
- 使用 `sqlite3` 模組寫入資料

📄 [SQLite 匯入程式碼 ➜ 點我看](./sqlite_insert.py)

**執行方式：**

- 執行匯入指令：  
  `python sqlite_insert.py`

---

## 📂 資料輸出格式一覽

- `professors.json`：JSON 格式儲存結果
- `professors.csv`：可直接開啟的 Excel 表格
- `professors.db`：儲存在 SQLite 資料庫中

