#!/usr/bin/python

# Copyright (c) 2020 Fernando
# Url: https://github.com/fernandod1/
# License: MIT

# คำอธิบาย:
# สคริปต์นี้ทำการตรวจสอบรูปภาพใหม่ที่ถูกโพสต์ในบัญชี Instagram
# และหากพบรูปภาพใหม่จะโพสต์รูปภาพนั้นในช่อง Discord
# และจะทำการตรวจสอบซ้ำหลังจากเวลาที่กำหนด

# สิ่งที่ต้องการ:
# - Python v3
# - Python โมดูล re, json, requests
import re
import json
import sys
import requests
import urllib.request
import os
import time

# วิธีใช้งาน:
# ตั้งค่าตัวแปรสภาพแวดล้อม:
# ตั้งค่าตัวแปร IG_USERNAME ให้เป็นชื่อผู้ใช้งาน Instagram ที่คุณต้องการตรวจสอบ เช่น ladygaga
# ตั้งค่าตัวแปร WEBHOOK_URL ให้เป็น URL ของ Discord webhook (หากไม่รู้วิธีสร้าง webhook บน Discord ให้ค้นหาใน Google)
# ตั้งค่า TIME_INTERVAL ให้เป็นเวลาในหน่วยวินาทีระหว่างการตรวจสอบแต่ละครั้ง เช่น 1.5, 600 (ค่าพื้นฐาน=600)
# วิธีการตั้งค่าตัวแปรสภาพแวดล้อม: https://www.serverlab.ca/tutorials/linux/administration-linux/how-to-set-environment-variables-in-linux/

INSTAGRAM_USERNAME = "ladygaga"  # เปลี่ยนให้เป็น Instagram username ที่คุณต้องการตรวจสอบ
WEBHOOK_URL = "https://discord.com/api/webhooks/your-webhook-url"  # เปลี่ยนให้เป็น URL ของ Discord webhook
TIME_INTERVAL = 600  # เวลาระหว่างการตรวจสอบ (ในหน่วยวินาที)

# ----------------------- ไม่ควรแก้ไขในส่วนนี้ ----------------------- #

def get_user_fullname(html):
    return html["graphql"]["user"]["full_name"]

def get_total_photos(html):
    return int(html["graphql"]["user"]["edge_owner_to_timeline_media"]["count"])

def get_last_publication_url(html):
    return html["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["shortcode"]

def get_last_photo_url(html):
    return html["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["display_url"]

def get_last_thumb_url(html):
    return html["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["thumbnail_src"]

def get_description_photo(html):
    return html["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"]

def webhook(webhook_url, html):
    # สำหรับพารามิเตอร์ทั้งหมด ดูได้ที่ https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    # สำหรับพารามิเตอร์ทั้งหมด ดูได้ที่ https://discordapp.com/developers/docs/resources/channel#embed-object
    data = {}
    data["embeds"] = []
    embed = {}
    embed["color"] = 15467852
    embed["title"] = "รูปภาพใหม่จาก @" + INSTAGRAM_USERNAME + ""
    embed["url"] = "https://www.instagram.com/p/" + get_last_publication_url(html) + "/"
    embed["description"] = get_description_photo(html)
    # embed["image"] = {"url":get_last_thumb_url(html)} # ลบเครื่องหมายคอมเมนต์เพื่อโพสต์ภาพขนาดใหญ่
    embed["thumbnail"] = {"url": get_last_thumb_url(html)}
    data["embeds"].append(embed)
    result = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("รูปภาพถูกโพสต์ใน Discord สำเร็จ รหัส {}.".format(result.status_code))

def get_instagram_html(INSTAGRAM_USERNAME):
    headers = {
        "Host": "www.instagram.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    response = requests.get("https://www.instagram.com/" + INSTAGRAM_USERNAME + "/feed/?__a=1", headers=headers)

    # ตรวจสอบการตอบกลับว่าเป็น HTTP 200 หรือไม่
    if response.status_code == 403:
        print("บัญชี Instagram ถูกจำกัดการเข้าถึงหรือถูกล็อค.")
        return None
    elif response.status_code == 429:
        print("เกิดข้อผิดพลาดจาก Instagram: การร้องขอมากเกินไป, โปรดลองใหม่ในภายหลัง.")
        return None
    elif response.status_code != 200:
        print(f"การเชื่อมต่อล้มเหลว! สถานะ: {response.status_code}")
        return None
    
    # ตรวจสอบว่าเนื้อหาที่ได้รับเป็น JSON หรือไม่
    try:
        json_data = response.json()
        return json_data
    except ValueError:
        print("ไม่สามารถแปลงข้อมูลเป็น JSON ได้.")
        return None

def main():
    try:
        html = get_instagram_html(INSTAGRAM_USERNAME)
        if html is None:
            print("ไม่สามารถดึงข้อมูลจาก Instagram ได้.")
            return
        
        last_image_id = os.getenv("LAST_IMAGE_ID")
        current_image_id = get_last_publication_url(html)
        
        if last_image_id == current_image_id:
            print("ไม่มีรูปภาพใหม่ที่จะโพสต์ใน Discord.")
        else:
            os.environ["LAST_IMAGE_ID"] = current_image_id
            print("พบรูปภาพใหม่ที่จะโพสต์ใน Discord.")
            webhook(WEBHOOK_URL, html)
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(TIME_INTERVAL)  # 600 = 10 นาที


