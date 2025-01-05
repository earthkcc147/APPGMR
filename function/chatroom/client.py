import sys
import socket
import select
import errno


HEADER_LENGTH = 10

IP = "192.168.204.1"
PORT = 5052
my_username = input("ชื่อผู้ใช้: ")

# สร้าง socket
# socket.AF_INET - address family, IPv4, ตัวเลือกอื่น ๆ เช่น AF_INET6, AF_BLUETOOTH, AF_UNIX
# socket.SOCK_STREAM - TCP, แบบเชื่อมต่อ, socket.SOCK_DGRAM - UDP, แบบไม่มีการเชื่อมต่อ, datagrams, socket.SOCK_RAW - raw IP packets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# เชื่อมต่อไปยัง IP และ PORT ที่กำหนด
client_socket.connect((IP, PORT))

# ตั้งค่าให้การเชื่อมต่อเป็น non-blocking เพื่อไม่ให้การเรียก .recv() ถูกบล็อก
client_socket.setblocking(False)

# เตรียมชื่อผู้ใช้และ header และส่งไปยัง server
# เราต้องแปลงชื่อผู้ใช้เป็น bytes, จากนั้นนับจำนวน bytes และเตรียม header ที่มีขนาดคงที่แล้วแปลงเป็น bytes
username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)

while True:

    # รอให้ผู้ใช้ป้อนข้อความ
    message = input(f'{my_username} > ')

    # หากข้อความไม่ว่าง ให้ส่งข้อความ
    if message:

        # แปลงข้อความเป็น bytes, เตรียม header และแปลงเป็น bytes, เหมือนที่ทำกับชื่อผู้ใช้ จากนั้นส่งไป
        message = message.encode('utf-8')
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)

    try:
        # ตอนนี้เราต้องการวนลูปเพื่อตรวจสอบข้อความที่ได้รับ (อาจมีมากกว่าหนึ่งข้อความ) และพิมพ์ออกมา
        while True:

            # รับ "header" ที่มีขนาดของชื่อผู้ใช้ ซึ่งขนาดจะถูกกำหนดไว้และคงที่
            username_header = client_socket.recv(HEADER_LENGTH)

            # หากไม่ได้รับข้อมูลใด ๆ แสดงว่า server ปิดการเชื่อมต่ออย่างสมบูรณ์ เช่น ใช้ socket.close() หรือ socket.shutdown(socket.SHUT_RDWR)
            if not len(username_header):
                print('การเชื่อมต่อถูกปิดโดยเซิร์ฟเวอร์')
                sys.exit()

            # แปลง header เป็นค่า int
            username_length = int(username_header.decode('utf-8').strip())

            # รับและแปลงชื่อผู้ใช้จาก bytes เป็นข้อความ
            username = client_socket.recv(username_length).decode('utf-8')

            # ทำเหมือนเดิมกับข้อความ (เมื่อเราได้รับชื่อผู้ใช้แล้ว เราก็จะได้รับข้อความทั้งหมด จึงไม่จำเป็นต้องตรวจสอบอีกว่าข้อความมีความยาวหรือไม่)
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode('utf-8').strip())
            message = client_socket.recv(message_length).decode('utf-8')

            # พิมพ์ข้อความ
            print(f'{username} > {message}')

    except IOError as e:
        # นี่เป็นเรื่องปกติสำหรับการเชื่อมต่อแบบ non-blocking - เมื่อไม่มีข้อมูลเข้ามาจะเกิดข้อผิดพลาด
        # บางระบบปฏิบัติการจะแจ้งว่าเป็น AGAIN และบางระบบจะแจ้งด้วยรหัสข้อผิดพลาด WOULDBLOCK
        # เราจะตรวจสอบทั้งสองกรณี - ถ้าเจอหนึ่งในนี้ หมายความว่าไม่มีข้อมูลเข้ามา ให้ดำเนินการต่อไปตามปกติ
        # ถ้าเจอรหัสข้อผิดพลาดอื่น ๆ แสดงว่าเกิดบางอย่างขึ้น
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('เกิดข้อผิดพลาดในการอ่าน: {}'.format(str(e)))
            sys.exit()

        # ถ้าไม่ได้รับข้อมูลอะไรมา
        continue

    except Exception as e:
        # หากมีข้อผิดพลาดอื่น ๆ - บางอย่างผิดปกติ ให้ปิดโปรแกรม
        print('เกิดข้อผิดพลาดในการอ่าน: {}'.format(str(e)))
        sys.exit()