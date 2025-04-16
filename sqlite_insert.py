import sqlite3
import json

# 創建資料庫連接
conn = sqlite3.connect('professors.db')
cursor = conn.cursor()

# 創建資料表
cursor.execute('''
CREATE TABLE IF NOT EXISTS professors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    expertise TEXT
)
''')

# 儲存資料
with open('professors_expertise.json', 'r', encoding='utf-8') as json_file:
    professors_data = json.load(json_file)
    for professor in professors_data:
        cursor.execute('''
        INSERT INTO professors (name, expertise) VALUES (?, ?)
        ''', (professor['姓名'], professor['專長領域']))

# 提交變更並關閉連接
conn.commit()
conn.close()
