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
# ตั้งค่าตัวแปรด้านล่างนี้ให้เป็นค่าที่คุณต้องการ

INSTAGRAM_USERNAME = "ชื่อผู้ใช้Instagram"  # ตั้งค่าชื่อผู้ใช้ Instagram ที่คุณต้องการตรวจสอบ
WEBHOOK_URL = "https://discord.com/api/webhooks/xxxx/xxxxx"  # ตั้งค่า Discord webhook URL ของคุณ
TIME_INTERVAL = 600  # ตั้งเวลาระหว่างการตรวจสอบ (ในหน่วยวินาที) เช่น 600 = 10 นาที

# ----------------------- ไม่ควรแก้ไขในส่วนนี้ ----------------------- #


def get_user_fullname(html):
    return html.json()["graphql"]["user"]["full_name"]


def get_total_photos(html):
    return int(html.json()["graphql"]["user"]["edge_owner_to_timeline_media"]["count"])


def get_last_publication_url(html):
    return html.json()["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["shortcode"]


def get_last_photo_url(html):
    return html.json()["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["display_url"]


def get_last_thumb_url(html):
    return html.json()["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["thumbnail_src"]


def get_description_photo(html):
    return html.json()["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"]


def webhook(webhook_url, html):
    # สำหรับพารามิเตอร์ทั้งหมด ดูได้ที่ https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    # สำหรับพารามิเตอร์ทั้งหมด ดูได้ที่ https://discordapp.com/developers/docs/resources/channel#embed-object
    data = {}
    data["embeds"] = []
    embed = {}
    embed["color"] = 15467852
    embed["title"] = "รูปภาพใหม่จาก @"+INSTAGRAM_USERNAME+""
    embed["url"] = "https://www.instagram.com/p/" + \
        get_last_publication_url(html)+"/"
    embed["description"] = get_description_photo(html)
    # embed["image"] = {"url":get_last_thumb_url(html)} # ลบเครื่องหมายคอมเมนต์เพื่อโพสต์ภาพขนาดใหญ่
    embed["thumbnail"] = {"url": get_last_thumb_url(html)}
    data["embeds"].append(embed)
    result = requests.post(webhook_url, data=json.dumps(
        data), headers={"Content-Type": "application/json"})
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("รูปภาพถูกโพสต์ใน Discord สำเร็จ รหัส {}.".format(
            result.status_code))


def get_instagram_html(INSTAGRAM_USERNAME):
    headers = {
        "Host": "www.instagram.com",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    html = requests.get("https://www.instagram.com/" +
                        INSTAGRAM_USERNAME + "/feed/?__a=1", headers=headers)
    return html


def main():
    try:
        html = get_instagram_html(INSTAGRAM_USERNAME)
        if(os.environ.get("LAST_IMAGE_ID") == get_last_publication_url(html)):
            print("ไม่มีรูปภาพใหม่ที่จะโพสต์ใน Discord.")
        else:
            os.environ["LAST_IMAGE_ID"] = get_last_publication_url(html)
            print("พบรูปภาพใหม่ที่จะโพสต์ใน Discord.")
            webhook(WEBHOOK_URL, get_instagram_html(INSTAGRAM_USERNAME))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    if INSTAGRAM_USERNAME != None and WEBHOOK_URL != None:
        while True:
            main()
            time.sleep(TIME_INTERVAL)  # 600 = 10 นาที
    else:
        print('โปรดตั้งค่าตัวแปรให้ถูกต้อง!')