# import modules urllib, thread, lock and queue  
import urllib.request, urllib.error
from threading import Thread, Lock
from queue import Queue

q = Queue()
list_lock = Lock()
discovered_usernames = []

# scan_sites from username
def scan_sites(username):
    global q
    while True:
        sites = q.get()
        url = f"{sites}{username}"
        try:
            conn = urllib.request.urlopen(url)
        # 404 error code, page does not exist
        except urllib.error.HTTPError as e:
            # create text file and save profile pages that dosent exist
            text_file = open(f"{username}""_ไม่พบโปรไฟล์.txt", "a")
            text_file.write(url)
            text_file.write("\n")
            text_file.close()
            print("[-] ไม่พบผู้ใช้ใน:", f"{sites}")
        # connection refused to site    
        except urllib.error.URLError as e:
            # create text file error_logs.txt and enter sites that refused to connect
            text_file = open("error_logs/บันทึกข้อผิดพลาด.txt", "a")
            text_file.write(url)
            text_file.write("\n")
            text_file.close()
            # show sites that refused to connect
            print('[!] ไม่สามารถเชื่อมต่อได้กับ', f"{sites}")
            pass
        else:
            # export found profile page urls to a text file
            text_file = open(f"{username}"".txt", "a")
            text_file.write(url)
            text_file.write("\n")
            text_file.close()  
            print("[+] พบผู้ใช้ใน", url)
            with list_lock:
                discovered_usernames.append(url)   
        q.task_done()

def main(username, n_threads, sites):
    global q

    for sites in sites:
        q.put(sites)   

    for t in range(n_threads):
        worker = Thread(target=scan_sites, args=(username,))
        worker.daemon = True
        worker.start()

if __name__ == "__main__":
    import argparse

    # Display main menu
    print("""
    ____  ____  ____  _____  ____  _____  __    __   ___  __    __
   |  _ \|  _ \|  _ \| ____|  _ \| ____|  \  /  |  / _ \|  \  /  |
   | |_) | |_) | |_) |  _|   | |_) |  _|     \/   | | | | |  \/  |  
   |  __/|  __/|  __/| |___  |  __/| |___    |    | |_| | |      |
   |_|   |_|   |_|   |_____| |_|   |_____|   |    |____/|_|      | 
   
# เครื่องมือ OSINT สำหรับสแกนบัญชีโซเชียลจากชื่อผู้ใช้
    """)      
    
    # รับค่า username จาก input ของผู้ใช้
    username = input("กรุณากรอกชื่อผู้ใช้ที่ต้องการค้นหา: ")
    
    # อ่าน URL จากไฟล์ res/sites.txt
    sitelist_file = "res/sites.txt"
    try:
        with open(sitelist_file, "r") as f:
            sitelist = f.read().splitlines()
    except FileNotFoundError:
        print(f"ไม่พบไฟล์ {sitelist_file}")
        exit(1)

    # รับค่าจำนวนเธรดจากผู้ใช้ หากไม่ได้กรอกให้ใช้ค่า default เป็น 10
    num_threads = input("กรุณากรอกจำนวนเธรดที่ต้องการใช้ในการสแกน (กด Enter เพื่อใช้ค่าเริ่มต้น 10): ")
    num_threads = int(num_threads) if num_threads else 10

    # เรียกใช้ฟังก์ชั่น main
    main(username=username, n_threads=num_threads, sites=sitelist)
    q.join()