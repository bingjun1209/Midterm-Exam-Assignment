# Midterm-Exam-Assignment
這次期中考作業，我研究了 `Selenium` 與 `Scrapy`，並嘗試抓取亞洲大學資訊工程學系的網頁老師的姓名與研究領域（專長）。
## ✅ 使用工具
- Python
- Selenium
- Scrapy
- CSV / JSON 檔案儲存
- SQLite
## 📌 抓取目標網站
---
[https://csie.asia.edu.tw/zh_tw/associate_professors_2](https://csie.asia.edu.tw/zh_tw/associate_professors_2)
---

## 🐍 首先使用 Selenium

使用 `Selenium` 自動打開網頁並擷取所有副教授的姓名與專長。資料可以儲存為下列兩個檔案(我是選擇csv)：
- `professors_expertise.csv`
- `professors_expertise.json`

📄 [Selenium 程式碼 → 點我看](./selenium_script.py)

---
## 🕷️ 接著使用 Scrapy

## 🕷️ 接著使用 Scrapy

使用 Scrapy 爬蟲框架自動抓取網頁中每位副教授的資料，並輸出為 csv 或 json。

📄 [Scrapy 程式碼 → 點我看](./csie_professors/spiders/professors.py)

### 🔧 執行爬蟲方式：

在專案根目錄下打開終端機，輸入以下指令：

#### ➤ 輸出成 JSON 格式
```bash
scrapy crawl professors -o professors.json


