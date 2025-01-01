import requests
import json

# รับข้อมูลหมายเลข, วันที่, เดือน และปี จากผู้ใช้
lottery_number = input("กรุณาป้อนหมายเลขสลาก (เช่น 123456): ")
date = input("กรุณาป้อนวันที่ (เช่น 01): ")
month = input("กรุณาป้อนเดือน (เช่น 03): ")
year = input("กรุณาป้อนปี (เช่น 2024): ")

# กำหนด URL และข้อมูลที่จะส่ง
url = "https://www.glo.or.th/api/checking/getLotteryResult"
data = {
    "date": date,
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
        print("\nผลการออกรางวัลสลากกินแบ่งรัฐบาล:")
        print(f"วันที่: {result['displayDate']}")
        print(f"ชุดที่: {result['period']}")
        print(f"ลิงก์ YouTube: {result['youtube_url']}")
        print(f"ลิงก์ PDF: {result['pdf_url']}")
        
        # ตรวจสอบหมายเลขที่ผู้ใช้กรอก
        found = False
        
        # ตรวจสอบรางวัลต่างๆ
        print("\nตรวจสอบหมายเลขที่ท่านกรอก:")
        
        # รางวัลที่ 1
        for number in result['data']['first']['number']:
            if lottery_number == number['value']:
                print(f"หมายเลข {lottery_number} ถูกรางวัลที่ 1 รางวัลละ {result['data']['first']['price']} บาท")
                found = True
        
        # รางวัลเลขหน้า 3 ตัว
        if not found:
            for number in result['data']['last3f']['number']:
                if lottery_number == number['value']:
                    print(f"หมายเลข {lottery_number} ถูกรางวัลเลขหน้า 3 ตัว รางวัลละ {result['data']['last3f']['price']} บาท")
                    found = True
        
        # รางวัลเลขท้าย 3 ตัว
        if not found:
            for number in result['data']['last3b']['number']:
                if lottery_number == number['value']:
                    print(f"หมายเลข {lottery_number} ถูกรางวัลเลขท้าย 3 ตัว รางวัลละ {result['data']['last3b']['price']} บาท")
                    found = True
        
        # รางวัลเลขท้าย 2 ตัว
        if not found:
            if lottery_number == result['data']['last2']['number'][0]['value']:
                print(f"หมายเลข {lottery_number} ถูกรางวัลเลขท้าย 2 ตัว รางวัลละ {result['data']['last2']['price']} บาท")
                found = True
        
        # รางวัลใกล้เคียงรางวัลที่ 1
        if not found:
            for number in result['data']['near1']['number']:
                if lottery_number == number['value']:
                    print(f"หมายเลข {lottery_number} ถูกรางวัลใกล้เคียงรางวัลที่ 1 รางวัลละ {result['data']['near1']['price']} บาท")
                    found = True
        
        # รางวัลที่ 2
        if not found:
            for number in result['data']['second']['number']:
                if lottery_number == number['value']:
                    print(f"หมายเลข {lottery_number} ถูกรางวัลที่ 2 รางวัลละ {result['data']['second']['price']} บาท")
                    found = True
        
        # รางวัลที่ 3
        if not found:
            for number in result['data']['third']['number']:
                if lottery_number == number['value']:
                    print(f"หมายเลข {lottery_number} ถูกรางวัลที่ 3 รางวัลละ {result['data']['third']['price']} บาท")
                    found = True
        
        # รางวัลที่ 4
        if not found:
            for number in result['data']['fourth']['number']:
                if lottery_number == number['value']:
                    print(f"หมายเลข {lottery_number} ถูกรางวัลที่ 4 รางวัลละ {result['data']['fourth']['price']} บาท")
                    found = True
        
        # รางวัลที่ 5
        if not found:
            for number in result['data']['fifth']['number']:
                if lottery_number == number['value']:
                    print(f"หมายเลข {lottery_number} ถูกรางวัลที่ 5 รางวัลละ {result['data']['fifth']['price']} บาท")
                    found = True
        
        # หากไม่พบหมายเลขที่กรอก
        if not found:
            print(f"หมายเลข {lottery_number} ไม่ถูกรางวัลในครั้งนี้")
        
    else:
        print("ไม่พบข้อมูลผลการออกรางวัลในคำตอบที่ได้")
else:
    print(f"เกิดข้อผิดพลาดในการร้องขอข้อมูล (HTTP Status: {response.status_code})")