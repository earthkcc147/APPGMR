import requests
import json
import datetime

# ฟังก์ชั่นที่ใช้ตรวจสอบวันที่
def get_lottery_date():
    today = datetime.date.today()  # รับวันที่ปัจจุบัน
    if today.day > 15:
        return 16
    else:
        return 1

# รับหมายเลขที่ต้องการตรวจสอบ
number = input("กรุณาป้อนหมายเลขที่ต้องการตรวจสอบ: ")

# ตรวจสอบวันที่
date = get_lottery_date()
month = str(datetime.date.today().month).zfill(2)  # รับเดือนปัจจุบัน
year = str(datetime.date.today().year)  # รับปีปัจจุบัน

# กำหนด URL และข้อมูลที่จะส่ง
url = "https://www.glo.or.th/api/checking/getLotteryResult"
data = {
    "date": str(date).zfill(2),  # เปลี่ยนวันที่ให้เป็นรูปแบบสองหลัก
    "month": month,
    "year": year
}

# ส่งคำขอ POST พร้อมข้อมูลในรูปแบบ JSON
response = requests.post(url, json=data)

# ตรวจสอบสถานะของการร้องขอ
if response.status_code == 200:
    # แปลงข้อมูล JSON เป็น Python dictionary
    result_data = response.json()
    if result_data.get("status") and "response" in result_data:
        result = result_data["response"]["result"]
        
        # แสดงผลข้อมูลจาก API
        print(f"\nผลการออกรางวัลสลากกินแบ่งรัฐบาล ประจำวันที่ {date}/{month}/{year}:")
        print(f"ชุดที่: {result['period']}")
        print(f"ลิงก์ YouTube: {result['youtube_url']}")
        print(f"ลิงก์ PDF: {result['pdf_url']}")
        
        # รางวัลต่างๆ
        print("\nรางวัลที่ 1:")
        print(f"หมายเลข: {result['data']['first']['number'][0]['value']}, รางวัลละ {result['data']['first']['price']} บาท")
        
        print("\nรางวัลเลขหน้า 3 ตัว:")
        for number in result['data']['last3f']['number']:
            print(f"หมายเลข: {number['value']}, รางวัลละ {result['data']['last3f']['price']} บาท")
        
        print("\nรางวัลเลขท้าย 3 ตัว:")
        for number in result['data']['last3b']['number']:
            print(f"หมายเลข: {number['value']}, รางวัลละ {result['data']['last3b']['price']} บาท")
        
        print("\nรางวัลเลขท้าย 2 ตัว:")
        print(f"หมายเลข: {result['data']['last2']['number'][0]['value']}, รางวัลละ {result['data']['last2']['price']} บาท")
        
        print("\nรางวัลใกล้เคียงรางวัลที่ 1:")
        for number in result['data']['near1']['number']:
            print(f"หมายเลข: {number['value']}, รางวัลละ {result['data']['near1']['price']} บาท")
        
        print("\nรางวัลที่ 2:")
        for number in result['data']['second']['number']:
            print(f"หมายเลข: {number['value']}, รางวัลละ {result['data']['second']['price']} บาท")
        
        print("\nรางวัลที่ 3:")
        for number in result['data']['third']['number']:
            print(f"หมายเลข: {number['value']}, รางวัลละ {result['data']['third']['price']} บาท")
        
        print("\nรางวัลที่ 4:")
        for number in result['data']['fourth']['number']:
            print(f"หมายเลข: {number['value']}, รางวัลละ {result['data']['fourth']['price']} บาท")
        
        print("\nรางวัลที่ 5:")
        for number in result['data']['fifth']['number']:
            print(f"หมายเลข: {number['value']}, รางวัลละ {result['data']['fifth']['price']} บาท")
    else:
        print("ไม่พบข้อมูลผลการออกรางวัลในคำตอบที่ได้")
else:
    print(f"เกิดข้อผิดพลาดในการร้องขอข้อมูล (HTTP Status: {response.status_code})")