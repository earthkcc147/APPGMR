"""ภาพยนตร์ยอดนิยมจาก IMDB ตามจำนวนที่กำหนด
"""
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os  # สำหรับการตรวจสอบและสร้างโฟลเดอร์

# ตรวจสอบว่าโฟลเดอร์ 'imdb' มีอยู่หรือไม่ ถ้าไม่มีก็สร้าง
folder_path = "imdb"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# รับค่าจำนวนภาพยนตร์ที่ต้องการดึงข้อมูล และตั้งค่า default เป็น 250
num_movies_input = input("กรุณากรอกจำนวนภาพยนตร์ที่ต้องการดึงข้อมูล (กด Enter เพื่อใช้ค่าเริ่มต้น 250): ")

# ถ้าผู้ใช้ไม่ได้กรอกค่า จะใช้ค่าเริ่มต้น 250
num_movies = int(num_movies_input) if num_movies_input else 250

URL = "http://www.imdb.com/chart/top"
RESPONSE = requests.get(URL)
SOUP = BeautifulSoup(RESPONSE.text, features="lxml")
MOVIES = SOUP.select("td.titleColumn")
STARS = [a.attrs.get("title") for a in SOUP.select("td.titleColumn a")]
RATINGS = []
for b in SOUP.select("td.posterColumn span[name=ir]"):
    RATINGS.append(round(float(b.attrs.get("data-value")), 1))

IMDB = []
# เก็บข้อมูลแต่ละรายการลงใน dictionary (data) แล้วนำไปเก็บในรายการ (imdb)
for index in range(0, num_movies):  # ใช้ num_movies เพื่อกำหนดจำนวนรายการที่ต้องการ
    movie_string = MOVIES[index].get_text()
    movie = " ".join(movie_string.split()).replace(".", "")
    movie_title = movie[len(str(index)) + 1 : -7]
    year = re.search(r"(.*?)", movie_string).group(1)
    data = {
        "ชื่อภาพยนตร์": movie_title,
        "ปีที่ฉาย": year,
        "นักแสดง": STARS[index],
        "คะแนน": RATINGS[index],
    }
    IMDB.append(data)

# สร้าง DataFrame
DF = pd.DataFrame(IMDB)
DF.index = DF.index.rename("ลำดับที่")
# คัดลอกข้อมูลจาก DataFrame ไปยังไฟล์ CSV ภายในโฟลเดอร์ imdb
csv_file_path = os.path.join(folder_path, "imdb.csv")
DF.to_csv(csv_file_path)
print(f"ไฟล์ CSV ได้ถูกสร้างขึ้นในโฟลเดอร์ '{folder_path}'")