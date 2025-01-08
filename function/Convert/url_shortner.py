__author__ = "Sri Manikanta Palakollu"
__date__ = "29-06-2020"

import requests
from urllib.parse import urlencode

def make_tiny(url):
    request_url = "http://tinyurl.com/api-create.php?" + urlencode({"url": url})
    result = requests.get(request_url)
    return result.text

def main():
    # รับ URL จากผู้ใช้
    url = input("กรุณากรอก URL ที่ต้องการย่อ: ")
    tinyurl = make_tiny(url)
    print(f"TinyURL: {tinyurl}")

if __name__ == "__main__":
    main()