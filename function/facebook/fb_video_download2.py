from datetime import datetime
from tqdm import tqdm
import requests
import re
import os

banner = r'''

  ___ ___  __   ___    _           ___                  _              _         
 | __| _ ) \ \ / (_)__| |___ ___  |   \ _____ __ ___ _ | |___  __ _ __| |___ _ _ 
 | _|| _ \  \ V /| / _` / -_) _ \ | |) / _ \ V  V / ' \| / _ \/ _` / _` / -_) '_|
 |_| |___/   \_/ |_\__,_\___\___/ |___/\___/\_/\_/|_||_|_\___/\__,_\__,_\___|_|  
                                                            [Coded by AnonyminHack5]

'''

print(banner)

def main_menu():
    print("\n----- เมนูหลัก -----")
    print("1. ดาวน์โหลดวิดีโอจาก Facebook")
    print("2. ออกจากโปรแกรม")
    choice = input("\nกรุณาเลือกตัวเลือก (1 หรือ 2): ")
    if choice == '1':
        download_facebook_video()
    elif choice == '2':
        print("\nขอบคุณที่ใช้โปรแกรม!")
        exit()
    else:
        print("\nกรุณาเลือกตัวเลือกที่ถูกต้อง")
        main_menu()

def download_facebook_video():
    try:
        url = input("\nกรุณากรอก URL ของวิดีโอจาก Facebook: ")
        x = re.match(r'^(https:|)[/][/]www.([^/]+[.])*facebook.com', url)

        if x:
            html = requests.get(url).content.decode('utf-8')
        else:
            print("\nURL นี้ไม่ใช่ของ Facebook.")
            return

        _qualityhd = re.search('hd_src:"https', html)
        _qualitysd = re.search('sd_src:"https', html)
        _hd = re.search('hd_src:null', html)
        _sd = re.search('sd_src:null', html)

        list = []
        _thelist = [_qualityhd, _qualitysd, _hd, _sd]
        for id, val in enumerate(_thelist):
            if val != None:
                list.append(id)

        video_quality_menu(list)

    except KeyboardInterrupt:
        print("\nโปรแกรมถูกหยุดชั่วคราว")
        main_menu()

def video_quality_menu(list):
    try:
        if len(list) == 2:
            if 0 in list and 1 in list:
                _input_1 = str(input("\nกด 'A' เพื่อดาวน์โหลดวิดีโอในคุณภาพ HD.\nกด 'B' เพื่อดาวน์โหลดวิดีโอในคุณภาพ SD.\n: ")).upper()
                if _input_1 == 'A':
                    download_video("HD")
                if _input_1 == 'B':
                    download_video("SD")

        if len(list) == 2:
            if 1 in list and 2 in list:
                _input_2 = str(input("\nอุ๊ปส์! วิดีโอนี้ไม่มีในคุณภาพ HD คุณต้องการดาวน์โหลดใน SD หรือไม่? ('Y' หรือ 'N'): ")).upper()
                if _input_2 == 'Y':
                    download_video("SD")
                if _input_2 == 'N':
                    main_menu()

        if len(list) == 2:
            if 0 in list and 3 in list:
                _input_2 = str(input("\nอุ๊ปส์! วิดีโอนี้ไม่มีในคุณภาพ SD คุณต้องการดาวน์โหลดใน HD หรือไม่? ('Y' หรือ 'N'): \n")).upper()
                if _input_2 == 'Y':
                    download_video("HD")
                if _input_2 == 'N':
                    main_menu()
    except(KeyboardInterrupt):
        print("\nโปรแกรมถูกหยุดชั่วคราว")
        main_menu()

def download_video(quality):
    """ดาวน์โหลดวิดีโอในคุณภาพ HD หรือ SD"""
    print(f"\nกำลังดาวน์โหลดวิดีโอในคุณภาพ {quality} ... \n")
    video_url = re.search(rf'{quality.lower()}_src:"(.+?)"', html).group(1)
    file_size_request = requests.get(video_url, stream=True)
    file_size = int(file_size_request.headers['Content-Length'])
    block_size = 1024
    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
    t = tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
    with open(filename + '.mp4', 'wb') as f:
        for data in file_size_request.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    print("\nดาวน์โหลดวิดีโอเสร็จสมบูรณ์.")
    main_menu()

try:
    main_menu()
except KeyboardInterrupt:
    print("\nโปรแกรมถูกหยุดชั่วคราว")