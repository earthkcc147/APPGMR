#--------------------------------#
# Copyright (c) 2022 Tekky#9999  #
#--------------------------------#

try:
    import random, os, threading, time, requests, sys
    from pystyle import *
except Exception as e:
    print(f'ERROR [{e}]')


class Main():
    try:
        def download(url):
            """
            ดาวน์โหลดวิดีโอ
            :param url:
            :return:
            """
            global x, videocount
            try:
                with open(f'./backup/tiktok{random.randint(1000, 9999)}.mp4', 'wb') as out_file:
                    videobytes = requests.get(f'{url}.mp4', stream=True)
                    out_file.write(videobytes.content)
                    x += 1
                    os.system(f"title BACKUP TOOL ^| Tekky#9999 ^| ดาวน์โหลดแล้ว: {x} ^| โฟลเดอร์: ./backup")
            except:
                pass


        def start():
            global x
            """
            ฟังก์ชันหลัก
            """

            os.system('cls' if os.name == 'nt' else "clear")
            os.system(f"title BACKUP TOOL ^| Tekky#9999 ^| สถานะ: กำลังโหลด")

            banner = """
                                .:                           :.                         
                              !?.            :   ~            ^J^                       
                            ?B!             G5   &&7            YG^                     
                          ?&G.      :^    .#@5   &@@&?  .^.      ^&#~                   
                        J@@!      ~5~    :&@@5   &@@@Y    ?Y.      5@#~                 
                        5@@7    !#G..Y~ ~@@@@5   &@@?      ~#G:    P@@!                 
                         ^&@B:7&@!.Y@@@B@@@@@5   &@@!        P@B^~&@G.                  
                           5@@@B^J@@@@@@@&&@@5   &@@!         ~&@@@!                    
                           5@@@5^@@@5.G@&:G@@5   &@@!       ...&@@@!                    
                         ~&@B:5@P:#@&  !. G@@5   &@@!      ??^&@!~&@B.                  
                        P@@7   ^&P.G@?    G@@5   &@@!    J&?:&B.   P@@7                 
                        J&@!     PP J&    G@@5   &@@!  ?@@^.B7     5@#~                 
                          ?&G.    ~? !!   B@@5   &@@?7&@&..Y.    ~&#^                   
                            7B!    .^     J@@5   &@@@@@G  ^    .YG^                     
                              !?.          &@5   &@@@@J       :?^                       
                                :.         ~@5   &@@@~       ..                         
                                            BP   &@&:                                   
                                            ^Y   &B.                                    
                                             :   7                                      
            """

            Anime.Fade(Center.Center(banner), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=3)
            Anime.Fade(Center.Center("เครื่องมือสำรองข้อมูล TikTok"), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=2)
            Anime.Fade(Center.Center("โดย Tekky#9999"), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=3)
            Anime.Fade(Center.Center("กรุณากรอก ID ที่เป็นรหัสสุ่มจากวิดีโอของบัญชีเป้าหมาย"), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=5)

            user = Write.Input(Center.Center("ID > "), Colors.blue_to_red, interval=0)

            os.system('cls' if os.name == 'nt' else "clear")
            print(Colorate.Vertical(Colors.blue_to_red, Center.Center("กำลังดาวน์โหลด...")))

            if not os.path.exists(f'backup'):
                os.makedirs(f'backup')

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
            }

            try:
                # เริ่มต้นการดึงข้อมูลจาก API
                response = requests.get(f"https://api.tiktokv.com/aweme/v1/multi/aweme/detail/?aweme_ids=%5B{user}%5D", headers=headers)
                response.raise_for_status()  # เพิ่มการตรวจสอบสถานะการตอบกลับ
                json_response = response.json()
                secUid = json_response["aweme_details"][0]["author"]["sec_uid"]
            except requests.exceptions.RequestException as e:
                print(f"Request error: {e}")
                return
            except requests.exceptions.JSONDecodeError as e:
                print(f"JSON decoding error: {e}")
                print("Response content:", response.text)  # แสดงข้อมูลที่ได้รับจาก API
                return

            max_cursor = "0"
            x = 0

            while True:
                try:
                    """
                    ทำการดึงวิดีโอจากบัญชีผู้ใช้
                    """

                    url = f"https://api16-core-c-useast1a.tiktokv.com/aweme/v1/aweme/post/?sec_user_id={secUid}&count=33&device_id=9999999999999999999&max_cursor={max_cursor}&aid=1180"
                    headers = {
                        "accept-encoding": "gzip",
                        "user-agent": "com.ss.android.ugc.trill/240303 (Linux; U; Android 12; en_US; Pixel 6 Pro; Build/SP2A.220405.004;tt-ok/3.10.0.2)",
                        "x-gorgon": "0"
                    }
                    response = requests.request("GET", url, headers=headers)
                    try:
                        if response.json()["status_msg"] == "No more videos":
                            break
                    except:
                        try:
                            max_cursor = response.json()["max_cursor"]
                        except:
                            break

                    videos = response.json()["aweme_list"]

                    for vid in videos:
                        url = vid["video"]["play_addr"]["url_list"][0]
                        threading.Thread(target=Main.download, args=(url,)).start()
                except:
                    print(Colorate.Vertical(Colors.blue_to_red, Center.Center("เสร็จสิ้น...")))
                    break

    except Exception as e:
        os.system('cls' if os.name == 'nt' else "clear")
        print(f'ERROR {e}')
        input()
        sys.exit()


if __name__ == '__main__':
    Main.start()