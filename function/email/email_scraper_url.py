# สคริปต์สำหรับดึงอีเมล์ทั้งหมดจากหน้าเว็บ

# นำเข้าไลบรารีและโมดูลที่ต้องการ
import re  # สำหรับการทำงานกับ Regular Expression
import requests  # สำหรับส่งคำขอ HTTP ไปยังเซิร์ฟเวอร์
from urllib.parse import urlsplit  # สำหรับแยกส่วนของ URL
from collections import deque  # คอนเทนเนอร์ที่คล้ายกับลิสต์

# แพ็คเกจ Python สำหรับการแยกและจัดการเอกสาร HTML และ XML
from bs4 import BeautifulSoup
import requests.exceptions  # สำหรับจัดการข้อยกเว้น

# ใส่ URL ของหน้าเว็บที่ต้องการดึงข้อมูลในตัวแปร original_url
original_url = input("กรุณากรอก URL ของหน้าเว็บ: ")

# คิวของ URL ที่ยังไม่ได้ถูกดึงข้อมูล
unprocessed_urls = deque([original_url])

# เซ็ตของ URL ที่ได้ถูกดึงข้อมูลแล้ว
processed_urls = set()

# เซ็ตของอีเมล์ที่ดึงมาได้
emails = set()

# แสดงข้อความเริ่มต้นการทำงาน
print("🔍 กำลังเริ่มดึงอีเมล์จากเว็บไซต์...")

# ย้าย URL ที่ยังไม่ได้ดึงข้อมูลจากคิวไปยังเซ็ตที่ถูกดึงข้อมูลแล้ว
url = unprocessed_urls.popleft()
# ลบและคืนค่าจากด้านซ้ายสุดของ deque
processed_urls.add(url)

# แยกส่วนของ URL เพื่อใช้ในการแก้ไขลิงก์ที่เป็น relative
parts = urlsplit(url)

# เนื่องจาก urlsplit() คืนค่ากลับเป็นทูเพิลที่ประกอบด้วย (schema, network location, path, query, fragment)
# เราจะใช้ส่วน base และ path สำหรับ URL ของเว็บไซต์
base_url = "{0.scheme}://{0.netloc}".format(parts)
path = url[: url.rfind("/") + 1] if "/" in parts.path else url

# ส่งคำขอ HTTP GET ไปยังเว็บไซต์
try:
    response = requests.get(url)
except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
    # ข้ามหน้าเว็บที่มีข้อผิดพลาดและไปยัง URL ถัดไป
    pass

# ดึงที่อยู่อีเมล์ทั้งหมดจากหน้าเว็บและเพิ่มลงในเซ็ต
new_emails = set(
    re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I)
)
emails.update(new_emails)

# แสดงอีเมล์ที่ดึงมาได้
if emails:
    print("\n📧 อีเมล์ที่พบจากเว็บไซต์:")
    for email in emails:
        print(f"➡️ {email}")
else:
    print("ไม่พบอีเมล์ในหน้าเว็บนี้.")

# ค้นหาทุก URL ที่เชื่อมโยงในหน้าเว็บ
# สร้าง BeautifulSoup เพื่อแยกเอกสาร HTML
soup = BeautifulSoup(response.text, "html.parser")

# เมื่อเอกสารนี้ถูกแยกและประมวลผลแล้ว
# ให้หาทุก ๆ แท็ก anchor (<a>) เพราะอาจมีอีเมล์หรือลิงก์เชื่อมโยง
for anchor in soup.find_all("a"):
    # ดึงลิงก์จากแท็ก anchor
    link = anchor.attrs["href"] if "href" in anchor.attrs else ""
    # แก้ไขลิงก์ที่เป็น relative (เริ่มต้นด้วย /)
    if link.startswith("/"):
        link = base_url + link
    elif not link.startswith("http"):
        link = path + link

    # เพิ่ม URL ใหม่ลงในคิวถ้ายังไม่ได้อยู่ในคิวหรือในเซ็ตที่ประมวลผลแล้ว
    if not link in unprocessed_urls and not link in processed_urls:
        unprocessed_urls.append(link)

# แสดงข้อความสิ้นสุดการทำงาน
print("\n🔄 การดึงอีเมล์เสร็จสมบูรณ์แล้ว!")
print("🚀 ขอบคุณที่ใช้บริการ.")