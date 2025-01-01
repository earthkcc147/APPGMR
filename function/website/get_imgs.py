import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse


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
    soup = bs(requests.get(url).content, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img"), "กำลังดึงข้อมูลรูปภาพ"):
        img_url = img.attrs.get("src")
        if not img_url:
            # หาก img ไม่มี attribute src ให้ข้าม
            continue
        # ทำให้ URL เป็น absolute โดยเชื่อมโดเมนกับ URL ที่ดึงมา
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
    return urls


def download(url, pathname):
    """
    ดาวน์โหลดไฟล์จาก URL และเก็บในโฟลเดอร์ `pathname`
    """
    # หาก path ยังไม่มี ให้สร้าง path
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # ดาวน์โหลดไฟล์แบบ chunk
    response = requests.get(url, stream=True)

    # ขนาดของไฟล์ทั้งหมด
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


def main(url, path):
    # ดึงรูปภาพทั้งหมด
    imgs = get_all_images(url)
    for img in imgs:
        # ดาวน์โหลดแต่ละรูปภาพ
        download(img, path)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="สคริปต์นี้ใช้สำหรับดาวน์โหลดรูปภาพทั้งหมดจากหน้าเว็บ")
    parser.add_argument("url", help="URL ของหน้าเว็บที่ต้องการดาวน์โหลดรูปภาพ")
    parser.add_argument("-p", "--path", help="โฟลเดอร์ที่ต้องการเก็บรูปภาพ (ค่าเริ่มต้นคือชื่อโดเมนของ URL)")

    args = parser.parse_args()
    url = args.url
    path = args.path

    if not path:
        # หากไม่ได้ระบุ path ใช้ชื่อโดเมนของ URL เป็นชื่อโฟลเดอร์
        path = urlparse(url).netloc

    main(url, path)




มีการสร้างโฟลเดอร์และไฟล์ไหม