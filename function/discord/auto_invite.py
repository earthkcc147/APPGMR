import aiohttp
import asyncio
from aioconsole import aprint
import ssl
import os

# โค้ดเชิญที่ต้องการใช้
code = "TwilightVault"

# ฟังก์ชันเพื่อสร้างไฟล์ proxies.txt และ tokens.txt ถ้ายังไม่มี
def create_files_if_not_exist():
    # สร้างไฟล์ proxies.txt ถ้ายังไม่มี
    if not os.path.exists("proxies.txt"):
        with open("proxies.txt", "w") as f:
            f.write("")  # เขียนเนื้อหาว่าง ๆ ไว้ในไฟล์
        aprint("สร้างไฟล์ proxies.txt")

    # สร้างไฟล์ tokens.txt ถ้ายังไม่มี
    if not os.path.exists("tokens.txt"):
        with open("tokens.txt", "w") as f:
            f.write("")  # เขียนเนื้อหาว่าง ๆ ไว้ในไฟล์
        aprint("สร้างไฟล์ tokens.txt")

async def main():
    # สร้างไฟล์ proxies.txt และ tokens.txt ถ้ายังไม่มี
    create_files_if_not_exist()

    # อ่าน token และ proxy จากไฟล์
    tokens = open("tokens.txt").read().splitlines()
    proxies = open("proxies.txt").read().splitlines()

    # ถ้ามี proxy ใช้ proxy ในการส่งคำขอ
    if len(proxies) > 0:
        for token, proxy in zip(tokens, proxies):
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                    'Accept': '*/*',
                    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Content-Type': 'application/json',
                    'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                    'Authorization': token,
                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                    'X-Discord-Locale': 'en-US',
                    'X-Debug-Options': 'bugReporterEnabled',
                    'Origin': 'https://discord.com',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Referer': 'https://discord.com',
                    'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'TE': 'trailers',
                }
                # ส่งคำขอ POST ไปยัง Discord API
                async with aiohttp.ClientSession() as session:
                    async with session.post(f"https://canary.discord.com/api/v9/invites/{code}", headers=headers, json={}, proxy=f"http://{proxy}") as resp:
                        if resp.status == 200:
                            await aprint("เข้าร่วมสำเร็จ")
                        elif resp.status == 429:
                            j = await resp.json()
                            await aprint(f"ถูกจำกัดการใช้งาน {j['retry_after']} วินาที")
                            await asyncio.sleep(j['retry_after'])
                        elif resp.status == 403:
                            await aprint("ถูกล็อค token")
                        else:
                            j = await resp.json()
                            await aprint(resp.status, j,)
                await asyncio.sleep(0.7)
            except Exception as e:
                await aprint(f"เกิดข้อผิดพลาด: {e}")
                continue
    # ถ้าไม่มี proxy ให้ใช้ token จากไฟล์ `tokens.txt` ทันที
    else:
        for token in tokens:
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                    'Accept': '*/*',
                    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Content-Type': 'application/json',
                    'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
                    'Authorization': token,
                    'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                    'X-Discord-Locale': 'en-US',
                    'X-Debug-Options': 'bugReporterEnabled',
                    'Origin': 'https://discord.com',
                    'DNT': '1',
                    'Connection': 'keep-alive',
                    'Referer': 'https://discord.com',
                    'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'TE': 'trailers',
                }
                # ส่งคำขอ POST ไปยัง Discord API โดยไม่มี proxy
                async with aiohttp.ClientSession() as session:
                    async with session.post(f"https://canary.discord.com/api/v9/invites/{code}", headers=headers, json={}) as resp:
                        if resp.status == 200:
                            await aprint("เข้าร่วมสำเร็จ")
                        elif resp.status == 429:
                            j = await resp.json()
                            await aprint(f"ถูกจำกัดการใช้งาน {j['retry_after']} วินาที")
                            await asyncio.sleep(j['retry_after'])
                        elif resp.status == 403:
                            await aprint("ถูกล็อค token")
                        else:
                            j = await resp.json()
                            await aprint(resp.status, j,)
                await asyncio.sleep(0.7)
            except Exception as e:
                await aprint(f"เกิดข้อผิดพลาด: {e}")
                continue

# เรียกใช้งานฟังก์ชันหลัก
asyncio.run(main())