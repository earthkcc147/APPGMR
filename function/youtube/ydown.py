import pytube
import colorama
import sys

red = colorama.Fore.RED
light_green = colorama.Fore.LIGHTGREEN_EX
green = colorama.Fore.GREEN

print(green, '''
 █████ █████     █████                                     ████                         █████                   
░░███ ░░███     ░░███                                     ░░███                        ░░███                    
 ░░███ ███    ███████   ██████  █████ ███ █████ ████████   ░███   ██████   ██████    ███████   ██████  ████████ 
  ░░█████    ███░░███  ███░░███░░███ ░███░░███ ░░███░░███  ░███  ███░░███ ░░░░░███  ███░░███  ███░░███░░███░░███
   ░░███    ░███ ░███ ░███ ░███ ░███ ░███ ░███  ░███ ░███  ░███ ░███ ░███  ███████ ░███ ░███ ░███████  ░███ ░░░ 
    ░███    ░███ ░███ ░███ ░███ ░░███████████   ░███ ░███  ░███ ░███ ░███ ███░░███ ░███ ░███ ░███░░░   ░███     
    █████   ░░████████░░██████   ░░████░████    ████ █████ █████░░██████ ░░████████░░████████░░██████  █████    
   ░░░░░     ░░░░░░░░  ░░░░░░     ░░░░ ░░░░    ░░░░ ░░░░░ ░░░░░  ░░░░░░   ░░░░░░░░  ░░░░░░░░  ░░░░░░  ░░░░░     
   
        ''')

try:
    if len(sys.argv) > 1:
        url = str(sys.argv[1])
        outpath = str(sys.argv[2])
    else:
        print(red, "การใช้งาน:", light_green, "python ydown.py URL DownloadPath")
        print(red, "ตัวอย่าง:", light_green, "python ydown.py \"https://www.youtube.com/watch?v"
                                                                  "=dQw4w9WgXcQ&ab_channel=RickAstley\" "
              "\"/root/Downloads/\"")
    if "youtube." in url:
        try:
            pytube.YouTube(url).streams.get_highest_resolution().download(str(outpath))
            print(light_green, "ดาวน์โหลดวิดีโอสำเร็จ:", 'ชื่อ: ', str(pytube.YouTube(url).title.format()))
            print(light_green, "ดาวน์โหลด:", "\"", str(pytube.YouTube(url).title), ".mp4\"", "ไปยัง ", str(outpath))
        except Exception as error:
            print(red, "เกิดข้อผิดพลาด: ", green, type(error).__name__, "–", error)

    else:
        print(red, "ข้อผิดพลาด: " + green, "URL ต้องเป็น URL ของ YouTube ที่ถูกต้อง")

except:
    sys.exit(1)