import requests
import json
from bs4 import BeautifulSoup
import os

def get_urls_from_json(filename="links.json"):
    """อ่าน URL จากไฟล์ JSON หากไม่พบจะสร้างไฟล์ใหม่พร้อมข้อมูลตัวอย่าง"""
    # ใช้ os.path.join เพื่อให้ไฟล์อยู่ในที่เดียวกับโปรแกรม
    filepath = os.path.join(os.getcwd(), filename)
    
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            return json.load(f)
    else:
        # สร้างไฟล์ใหม่พร้อม URL ตัวอย่าง
        example_urls = [
            'https://b2c-api-premiumlabel-production.azurewebsites.net/api/b2c/page/menu?id_loja=2691',
            'https://b2c-api-premiumlabel-production.azurewebsites.net/api/b2c/page/menu?id_loja=2692',
            'https://b2c-api-premiumlabel-production.azurewebsites.net/api/b2c/page/menu?id_loja=2693'
        ]
        with open(filepath, 'w') as f:
            json.dump(example_urls, f, indent=4)
        return example_urls

def fetch_links(url):
    """ดึงข้อมูลลิงก์จาก URL และแสดงผลลัพธ์"""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("a")  # list of all items with this selector

    sites = []
    for link in links:
        sites.append(link.get('href'))  # ดึงแค่ URL จาก attribute 'href'

    return sites

def main():
    print("1. รับ URL จากผู้ใช้")
    print("2. ใช้ URL จากไฟล์ links.json")

    choice = input("เลือกตัวเลือก (1/2): ")

    if choice == "1":
        # รับ URL จากผู้ใช้
        url = input("กรุณากรอก URL: ")
        links = fetch_links(url)
    elif choice == "2":
        # ใช้ URL จากไฟล์ links.json
        urls = get_urls_from_json()
        for url in urls:
            print(f"กำลังดึงลิงก์จาก {url}...")
            links = fetch_links(url)
            print(f"ลิงก์ที่พบ: {links}")
    else:
        print("ตัวเลือกไม่ถูกต้อง")
        return

    # แสดงลิงก์ที่ดึงได้
    print("\nลิงก์ที่ดึงได้:")
    for link in links:
        print(link)

if __name__ == "__main__":
    main()