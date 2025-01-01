''' pip install requests_html '''

from requests_html import HTMLSession
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse

import os


def is_valid(url):
    """
    ตรวจสอบว่า `url` เป็น URL ที่ถูกต้องหรือไม่
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_images(url):
    """
    ดึง URL ของรูปภาพทั้งหมดจากหน้าเว็บ `url`
    """
    # เริ่มต้น session
    session = HTMLSession()
    # ทำการร้องขอ HTTP และรับข้อมูลตอบกลับ
    response = session.get(url)
    # ทำให้ Javascript รันด้วยเวลา 20 วินาที
    response.html.render(timeout=20)
    # สร้าง parser ด้วย BeautifulSoup
    soup = bs(response.html.html, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img"), "กำลังดึงข้อมูลรูปภาพ"):
        img_url = img.attrs.get("src") or img.attrs.get("data-src") or img.attrs.get("data-original")
        print(img_url)
        if not img_url:
            # หากไม่พบ attribute src ให้ข้ามไป
            continue
        # ทำให้ URL เป็น absolute โดยการรวมโดเมนกับ URL ที่ดึงมา
        img_url = urljoin(url, img_url)
        # ลบ URL ที่มีลักษณะเช่น '/hsts-pixel.gif?c=3.2.5'
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        # หาก URL ถูกต้อง
        if is_valid(img_url):
            urls.append(img_url)
    # ปิด session หลังจากการทำงานเสร็จ
    session.close()
    return urls


def download(url, pathname):
    """
    ดาวน์โหลดไฟล์จาก URL และเก็บในโฟลเดอร์ `pathname`
    """
    # หากโฟลเดอร์ยังไม่มีก็ให้สร้างโฟลเดอร์
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # ดาวน์โหลดไฟล์โดยใช้ chunk
    response = requests.get(url, stream=True)

    # ขนาดไฟล์ทั้งหมด
    file_size = int(response.headers.get("Content-Length", 0))

    # ชื่อไฟล์
    filename = os.path.join(pathname, url.split("/")[-1])

    # แสดง progress bar
    progress = tqdm(response.iter_content(1024), f"กำลังดาวน์โหลด {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            # เขียนข้อมูลลงไฟล์
            f.write(data)
            # อัปเดต progress bar
            progress.update(len(data))


def main():
    # รับ URL จากผู้ใช้
    url = input("กรุณากรอก URL ของหน้าเว็บที่ต้องการดาวน์โหลดรูปภาพ: ")

    # รับ path จากผู้ใช้ (หากไม่ระบุให้ใช้ชื่อโดเมนจาก URL)
    path = input("กรุณากรอกโฟลเดอร์ที่ต้องการเก็บรูปภาพ (กด Enter เพื่อใช้ค่าเริ่มต้น): ")

    if not path:
        # หากไม่ได้ระบุ path ใช้ชื่อโดเมนของ URL เป็นชื่อโฟลเดอร์
        path = urlparse(url).netloc

    # ดึงรูปภาพทั้งหมด
    imgs = get_all_images(url)
    for img in imgs:
        # ดาวน์โหลดแต่ละรูปภาพ
        download(img, path)


if __name__ == "__main__":
    main()