import socket
import select

HEADER_LENGTH = 10

IP = "192.168.204.1"
PORT = 5052

# สร้าง socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ตั้งค่า REUSEADDR (เป็นตัวเลือก socket) เป็น 1
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# ผูก IP และ PORT ให้กับ server
server_socket.bind((IP, PORT))

# ทำให้ server เริ่มฟังการเชื่อมต่อ
server_socket.listen()

# รายการของ socket ที่จะตรวจสอบด้วย select.select()
sockets_list = [server_socket]

# รายการของผู้ใช้ที่เชื่อมต่อ - ใช้ socket เป็น key และเก็บข้อมูล header กับชื่อผู้ใช้
clients = {}

print(f'กำลังรอฟังการเชื่อมต่อที่ {IP}:{PORT}...')

# ฟังก์ชันรับข้อความ
def receive_message(client_socket):

    try:
        # รับ "header" ที่เก็บขนาดข้อความ
        message_header = client_socket.recv(HEADER_LENGTH)

        # หากไม่ได้รับข้อมูลใด ๆ แสดงว่า client ปิดการเชื่อมต่อ
        if not len(message_header):
            return False

        # แปลง header เป็นค่าจำนวนเต็ม
        message_length = int(message_header.decode('utf-8').strip())

        # คืนค่าผลลัพธ์เป็น header และข้อความ
        return {'header': message_header, 'data': client_socket.recv(message_length)}

    except:
        # หากเกิดข้อผิดพลาด แสดงว่า client ปิดการเชื่อมต่ออย่างกะทันหัน
        return False

while True:

    # ใช้ select.select() เพื่อรอการรับข้อมูลจาก socket
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    # ตรวจสอบ socket ที่มีข้อมูลใหม่
    for notified_socket in read_sockets:

        # หาก socket ที่แจ้งเตือนเป็น server socket แสดงว่าเป็นการเชื่อมต่อใหม่
        if notified_socket == server_socket:

            # ยอมรับการเชื่อมต่อใหม่
            client_socket, client_address = server_socket.accept()

            # รับชื่อผู้ใช้จาก client
            user = receive_message(client_socket)

            # หากไม่พบชื่อผู้ใช้ แสดงว่า client ปิดการเชื่อมต่อ
            if user is False:
                continue

            # เพิ่ม socket ใหม่ในรายการที่จะตรวจสอบ
            sockets_list.append(client_socket)

            # เก็บข้อมูลชื่อผู้ใช้
            clients[client_socket] = user

            print(f'การเชื่อมต่อใหม่จาก {client_address[0]}:{client_address[1]}, ชื่อผู้ใช้: {user["data"].decode("utf-8")}')

        # หาก socket ที่แจ้งเตือนเป็น socket ของผู้ใช้ที่เชื่อมต่ออยู่
        else:

            # รับข้อความจาก client
            message = receive_message(notified_socket)

            # หากไม่พบข้อความ แสดงว่า client ปิดการเชื่อมต่อ
            if message is False:
                print(f'ปิดการเชื่อมต่อจาก: {clients[notified_socket]["data"].decode("utf-8")}')

                # ลบ socket ออกจากรายการ
                sockets_list.remove(notified_socket)

                # ลบผู้ใช้จากรายการ
                del clients[notified_socket]

                continue

            # ได้รับข้อมูลผู้ใช้จาก socket ที่แจ้งเตือน
            user = clients[notified_socket]

            print(f'ได้รับข้อความจาก {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

            # ส่งข้อความไปยังผู้ใช้ทุกคน
            for client_socket in clients:

                # ไม่ส่งข้อความไปยังผู้ส่ง
                if client_socket != notified_socket:

                    # ส่งทั้ง header ของผู้ใช้และข้อความ
                    client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    # จัดการข้อผิดพลาดของ socket (เช่น การปิดการเชื่อมต่อผิดปกติ)
    for notified_socket in exception_sockets:

        # ลบ socket ออกจากรายการ
        sockets_list.remove(notified_socket)

        # ลบผู้ใช้จากรายการ
        del clients[notified_socket]