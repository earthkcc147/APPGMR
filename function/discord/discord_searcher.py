import os, discord, re
from colorama import Fore, init

client = discord.Client()
init()

# ตั้งค่าภายในโค้ด
token = "YOUR DISCORD TOKEN"  # ใส่ token ของ Discord ที่ต้องการใช้
servers_enabled = True  # กำหนดว่าจะสแกนเซิร์ฟเวอร์หรือไม่
dm_enabled = True  # กำหนดว่าจะสแกน DM หรือไม่
words_to_search = [
    "Message to search",
    "Other message to search"
]  # คำที่ต้องการค้นหา
regex_patterns = [
    "Regex Use for search a custom message",
    "Other regex"
]  # รูปแบบ regex ที่ต้องการค้นหา

def center(var: str, space: int = None):  # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines()) / 2)])) / 2
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

class Console():
    def main(self, username, id):
        os.system('cls && title Discord Message Searcher - Made By Kaneki Web')
        print(center(f"""

    ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗███████╗██████╗ 
    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
    ███████╗█████╗  ███████║██████╔╝██║     ███████║█████╗  ██████╔╝  
    ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  ██╔══██╗
    ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║  
    ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝


            เข้าสู่ระบบโดย: {Fore.CYAN + username + Fore.RESET} ({Fore.CYAN + id + Fore.RESET})

        """).replace('█', Fore.RED + "█" + Fore.RESET))


@client.event
async def on_ready():
    Console().main(str(client.user), str(client.user.id))
    serveur_count = 0
    channels_count = 0
    messages_count = 0
    dm_count = 0

    # ตรวจสอบและสร้างไฟล์ found.txt หากไม่พบ
    if not os.path.exists('found.txt'):
        open('found.txt', 'w').close()

    if servers_enabled:  # เช็คว่าควรสแกนเซิร์ฟเวอร์หรือไม่
        for guild in client.guilds:
            print(f"[{Fore.RED}SERVER{Fore.RESET}] กำลังสแกนเซิร์ฟเวอร์: " + guild.name + " "*30)
            serveur_count += 1
            for channel in guild.text_channels:
                print(f"[{Fore.CYAN}CHANNEL{Fore.RESET}] กำลังสแกนช่อง: " + channel.name + " "*30, end="\r")
                channels_count += 1
                try:
                    async for message in client.get_channel(channel.id).history(limit=99999):
                        messages_count += 1
                        for searchmessage in words_to_search:
                            if searchmessage in message.content:
                                print(f"[{Fore.GREEN}MESSAGE{Fore.RESET}] พบข้อความ: " + message.content)
                                open('found.txt', 'a+').write(f"{message.author.name}: {message.content}\n")

                        for regex in regex_patterns:
                            if re.match(r"" + regex, message.content):
                                print(f"[{Fore.GREEN}MESSAGE{Fore.RESET}] พบข้อความ: " + message.content)
                                open('found.txt', 'a+').write(f"{message.author.name}: {message.content}\n")
                except:
                    pass

    if dm_enabled:  # เช็คว่าควรสแกน DM หรือไม่
        for prv_channel in client.private_channels:
            channels_count += 1
            dm_count += 1
            print(f"[{Fore.CYAN}CHANNEL{Fore.RESET}] กำลังสแกน DM: {str(prv_channel).replace('Direct Message with ', '')}" + " "*30, end="\r")
            channel = client.get_channel(prv_channel.id)
            try:
                async for message in channel.history(limit=99999):
                    messages_count += 1
                    for searchmessage in words_to_search:
                        if searchmessage in message.content:
                            print(f"[{Fore.GREEN}MESSAGE{Fore.RESET}] พบข้อความ: " + message.content)
                            open('found.txt', 'a+').write(f"{message.author.name}: {message.content}\n")

                    for regex in regex_patterns:
                        if re.match(r"" + regex, message.content):
                            print(f"[{Fore.GREEN}MESSAGE{Fore.RESET}] พบข้อความ: " + message.content)
                            open('found.txt', 'a+').write(f"{message.author.name}: {message.content}\n")
            except:
                pass

    input(f"{Fore.RED+str(messages_count)+Fore.RESET} ข้อความได้ถูกสแกนจาก {Fore.RED+str(channels_count)+Fore.RESET} ช่อง ({Fore.RED+str(serveur_count)+Fore.RESET} เซิร์ฟเวอร์, {Fore.RED+str(dm_count)+Fore.RESET} DM)")

client.run(token, bot=False)



