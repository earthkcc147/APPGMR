#GMR

import os
from telethon import TelegramClient
import asyncio

# ชื่อไฟล์เซสชัน
# session_file = 'session_name.session'

# ลบไฟล์เซสชันถ้ามี
# if os.path.exists(session_file):
#     os.remove(session_file)
#     print("ไฟล์เซสชันถูกลบเรียบร้อยแล้ว")

# ตั้งค่าข้อมูลที่ได้รับจาก Telegram
api_id = '24526330'  # แทนที่ด้วย api_id ของคุณ
api_hash = '7e6566f5cb575553cd0ddc18f5f3bb1a'  # แทนที่ด้วย api_hash ของคุณ
phone_number = '0841304874'  # หมายเลขโทรศัพท์ของคุณ

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)  # จะมีการขอให้ป้อน OTP ใหม่
    print("เข้าสู่ระบบเรียบร้อยในชื่อ:", await client.get_me())

    # ตรวจสอบกลุ่มที่มีอยู่
    dialogs = await client.get_dialogs()

    print("กลุ่มและช่องสนทนาที่คุณเข้าร่วม:")
    groups_info = []
    for dialog in dialogs:
        if dialog.is_group or dialog.is_channel:
            # ดึงข้อมูลเพิ่มเติมเกี่ยวกับกลุ่ม
            entity = await client.get_entity(dialog.id)
            date_joined = entity.date  # วันที่เข้าร่วมกลุ่ม
            groups_info.append((dialog.name, dialog.id, date_joined))
            print(f"- {dialog.name} (ID: {dialog.id}, วันที่เข้าร่วม: {date_joined})")
            
            # สร้างลิงก์เชิญใหม่สำหรับกลุ่ม
            try:
                invite_link = await client(functions.messages.ExportChatInviteLinkRequest(dialog.id))
                print(f"ลิงก์เชิญสำหรับ {dialog.name}: {invite_link}")
            except Exception as e:
                print(f"ไม่สามารถสร้างลิงก์เชิญสำหรับ {dialog.name}: {str(e)}")
    
    # user_id ของผู้ใช้ที่ต้องการส่งข้อความ
    user_id = 6757863220  # แทนที่ด้วย user_id ของผู้ใช้ที่ต้องการส่งข้อความ

    # สร้างข้อความที่จะส่งไปยังผู้ใช้
    message = "กลุ่มที่คุณเข้าร่วม:\n"
    for group_name, group_id, date_joined in groups_info:
        message += f"{group_name} (ID: {group_id}, วันที่เข้าร่วม: {date_joined.strftime('%Y-%m-%d %H:%M:%S')})\n"

    # ส่งข้อความหาผู้ใช้
    await client.send_message(user_id, message)

    print(f"ข้อความกลุ่มถูกส่งไปยังผู้ใช้ที่มี ID: {user_id}")

# เรียกใช้ client
with client:
    client.loop.run_until_complete(main())