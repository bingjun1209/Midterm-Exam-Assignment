from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import json
import time

# 設定 ChromeDriver 路徑
driver_path = '/path/to/chromedriver'  # 請換成你的 chromedriver 路徑
driver = webdriver.Chrome(executable_path=driver_path)

# 設定目標網址
url = "https://csie.asia.edu.tw/zh_tw/associate_professors_2"
driver.get(url)

# 給網頁一些時間來加載
time.sleep(3)

# 找到所有副教授的資料區塊
professors = driver.find_elements(By.CLASS_NAME, 'views-row')

# 儲存為 CSV 格式
csv_file = 'professors_expertise.csv'

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['姓名', '專長領域'])

    for professor in professors:
        name_tag = professor.find_element(By.CSS_SELECTOR, '.field-content')
        name = name_tag.text.strip() if name_tag else 'N/A'

        expertise_tag = professor.find_element(By.CSS_SELECTOR, '.field-name-field-professor-expertise')
        expertise = expertise_tag.text.strip() if expertise_tag else 'N/A'

        writer.writerow([name, expertise])

# 儲存為 JSON 格式
json_data = []
for professor in professors:
    name_tag = professor.find_element(By.CSS_SELECTOR, '.field-content')
    name = name_tag.text.strip() if name_tag else 'N/A'

    expertise_tag = professor.find_element(By.CSS_SELECTOR, '.field-name-field-professor-expertise')
    expertise = expertise_tag.text.strip() if expertise_tag else 'N/A'

    json_data.append({
        '姓名': name,
        '專長領域': expertise
    })

with open('professors_expertise.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

driver.quit()
print(f"資料已儲存至 {csv_file} 和 professors_expertise.json")
