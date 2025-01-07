import sys
from tqdm import tqdm
from requests import get, HTTPError, ConnectionError
from re import findall
from urllib.parse import unquote


def Invalid_Url():
    """แสดงข้อความผิดพลาดกรณี URL ไม่ถูกต้อง"""
    print("URL ไม่ถูกต้อง, กรุณากรอก URL ให้ถูกต้อง")


def get_video_downloadlink(url):
    """ดึงลิงค์ดาวน์โหลดวิดีโอจาก URL ที่ได้รับ"""
    url = url.replace("www", "mbasic")  # เปลี่ยน URL ไปยังเวอร์ชันมือถือ
    try:
        r = get(url, timeout=5, allow_redirects=True)  # ส่งคำขอไปยัง URL
        if r.status_code != 200:
            raise HTTPError  # ถ้าไม่ตอบกลับสถานะ 200 จะเกิดข้อผิดพลาด
        a = findall("/video_redirect/", r.text)  # ค้นหาคำว่า "/video_redirect/"
        if len(a) == 0:
            print("[!] ไม่พบวิดีโอ...")
            sys.exit(0)
        else:
            return unquote(r.text.split("?src=")[1].split('"')[0])  # คืนค่าลิงค์ดาวน์โหลด
    except (HTTPError, ConnectionError):
        print("[x] URL ไม่ถูกต้อง")
        sys.exit(1)


def download_video(url):
    """ดาวน์โหลดวิดีโอจาก URL ที่ได้รับ"""
    block_size = 1024  # ขนาดบล็อคในการดาวน์โหลด (1kB)
    r = get(url, stream=True)  # ส่งคำขอให้ดาวน์โหลดไฟล์
    total_size = int(r.headers.get("content-length"))  # ขนาดไฟล์ทั้งหมด
    progress_bar = tqdm(total=total_size, unit="iB", unit_scale=True)  # แสดงแถบความคืบหน้า
    with open("video.mp4", "wb") as file:
        for data in r.iter_content(block_size):  # อ่านข้อมูลในบล็อค
            progress_bar.update(len(data))  # อัปเดตแถบความคืบหน้า
            file.write(data)  # เขียนข้อมูลลงไฟล์
    progress_bar.close()  # ปิดแถบความคืบหน้า
    print("ดาวน์โหลดวิดีโอเสร็จสิ้น")
    if total_size != 0 and progress_bar.n != total_size:  # ตรวจสอบว่าไฟล์ถูกดาวน์โหลดครบหรือไม่
        print("เกิดข้อผิดพลาด, มีบางอย่างผิดพลาด")


def main():
    """ฟังก์ชันหลักสำหรับรับ URL และดาวน์โหลดวิดีโอ"""
    url = input("กรุณากรอก URL ของวิดีโอจาก Facebook ที่ต้องการดาวน์โหลด: ")
    if not "www.facebook.com" in url:  # ตรวจสอบว่า URL เป็นของ Facebook หรือไม่
        Invalid_Url()
        return

    link = get_video_downloadlink(url)  # รับลิงค์ดาวน์โหลด
    download_video(link)  # ดาวน์โหลดวิดีโอ


if __name__ == "__main__":
    main()  # เรียกฟังก์ชันหลัก