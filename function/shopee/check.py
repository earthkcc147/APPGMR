from datetime import date
import time
import requests
import json

# พิมพ์วันที่เพื่อให้ผู้ใช้ทราบว่าไฟล์ถูกสร้างเมื่อใด
วันที่ = date.today()
วันที่.strftime("%d/%m/%Y")
วันนี้ = date.today()

# ขอรหัสผู้ขาย
รหัสผู้ขาย = input('กรุณากรอกรหัสผู้ขาย: \n')

url_api_request = 'https://shopee.com.br/api/v4/recommend/recommend?bundle=shop_page_product_tab_main&limit=999&offset=0&section=shop_page_product_tab_main_sec&shopid=' + รหัสผู้ขาย
r = requests.get(url_api_request)

# กำหนดจำนวนสินค้า
จำนวนสินค้า = (r.json()['data']['sections'][0]['data']['item'])
ขนาดรายการ = len(จำนวนสินค้า)

# สร้างลูป while เพื่อดึงข้อมูลสินค้า เนื่องจาก index ของ json เริ่มต้นที่ 0 ลูปจึงเริ่มต้นที่ -1
ข้อมูลทั้งหมด = []
สร้าง_ลูป = -1
while สร้าง_ลูป < ขนาดรายการ - 1:
    สร้าง_ลูป += 1

    # เก็บข้อมูลจาก json
    รหัสสินค้า = (r.json()['data']['sections'][0]['data']['item'][สร้าง_ลูป]['itemid'])
    ชื่อสินค้า = (r.json()['data']['sections'][0]['data']['item'][สร้าง_ลูป]['name'])
    คงคลัง = (r.json()['data']['sections'][0]['data']['item'][สร้าง_ลูป]['stock'])
    ยอดขาย = (r.json()['data']['sections'][0]['data']['item'][สร้าง_ลูป]['historical_sold'])
    ชอบ = (r.json()['data']['sections'][0]['data']['item'][สร้าง_ลูป]['liked_count'])
    จำนวนดู = (r.json()['data']['sections'][0]['data']['item'][สร้าง_ลูป]['view_count'])
    ราคา = (r.json()['data']['sections'][0]['data']['item'][สร้าง_ลูป]['price'])
    คะแนน = (r.json()['data']['sections'][0]['data']['item'][สร้าง_ลูป]['item_rating']['rating_count'][0])
    time.sleep(1)

    # เก็บข้อมูลในรูปแบบ dictionary
    ข้อมูลสินค้า = {
        "ad_id": รหัสสินค้า,
        "title": ชื่อสินค้า,
        "stock": คงคลัง,
        "price": ราคา,
        "sales": ยอดขาย,
        "rating": คะแนน,
        "likes": ชอบ,
        "views": จำนวนดู
    }

    # เพิ่มข้อมูลสินค้าลงใน list
    ข้อมูลทั้งหมด.append(ข้อมูลสินค้า)

# แสดงข้อมูลทั้งหมดในรูปแบบ JSON บน terminal
print(json.dumps(ข้อมูลทั้งหมด, ensure_ascii=False, indent=4))

print('การดึงข้อมูลเสร็จสิ้น! ข้อมูลแสดงบน terminal แล้ว!')