import re
import requests
from bs4 import BeautifulSoup


def parseURL(url):
    return url.replace("&amp;", "&")


def extractLinks(url):
    # ดึงลิงก์จากหน้าเว็บที่กำหนด

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    links = re.findall("http.?://[^\s\"']+", str(soup))

    if len(links) == 0:
        print("ไม่พบลิงก์ใน {}".format(url))

    for link in links:
        print(parseURL(link))


if __name__ == "__main__":
    # รับค่า URL จากผู้ใช้
    url = input("กรุณากรอก URL ที่ต้องการค้นหาลิงก์: ")

    if url:
        extractLinks(url)
    else:
        print("กรุณากรอก URL!")