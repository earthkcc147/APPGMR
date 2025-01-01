import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

def extract_js_css_and_html_scripts(url):
    session = requests.Session()
    session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    html = session.get(url).content
    soup = bs(html, "html.parser")
    script_files = []
    css_files = []
    html_scripts = []

    for script in soup.find_all("script"):
        if script.attrs.get("src"):
            script_url = urljoin(url, script.attrs.get("src"))
            script_files.append(script_url)
        else:
            # หาก script ไม่มี attribute src ถือว่าเป็น HTML script inline
            html_script = script.text
            html_scripts.append(html_script)

    for css in soup.find_all("link"):
        if css.attrs.get("href"):
            css_url = urljoin(url, css.attrs.get("href"))
            css_files.append(css_url)

    if script_files:
        print("พบไฟล์ JavaScript ทั้งหมดในหน้าเว็บ:", len(script_files))
        with open("javascript_files.txt", "w", encoding="utf-8") as f:
            for js_file in script_files:
                print(js_file, file=f)
    else:
        print("ไม่พบไฟล์ JavaScript ในหน้าเว็บ.")

    if css_files:
        print("พบไฟล์ CSS ทั้งหมดในหน้าเว็บ:", len(css_files))
        with open("css_files.txt", "w", encoding="utf-8") as f:
            for css_file in css_files:
                print(css_file, file=f)
    else:
        print("ไม่พบไฟล์ CSS ในหน้าเว็บ.")

    if html_scripts:
        print("พบ HTML Scripts ทั้งหมดในหน้าเว็บ:", len(html_scripts))
        with open("html_scripts.txt", "w", encoding="utf-8") as f:
            for html_script in html_scripts:
                print(html_script, file=f)
    else:
        print("ไม่พบ HTML Scripts ในหน้าเว็บ.")

if __name__ == "__main__":
    url = input("กรุณาใส่ URL ที่ต้องการดึงข้อมูล JavaScript, CSS และ HTML Scripts: ")
    extract_js_css_and_html_scripts(url)