import os
from telethon import TelegramClient, functions
import asyncio

# ชื่อไฟล์เซสชัน
session_file = 'session_name.session'

# ลบไฟล์เซสชันถ้ามี
# Uncomment this if you want to delete the session file each time
if os.path.exists(session_file):
    os.remove(session_file)
    print("ไฟล์เซสชันถูกลบเรียบร้อยแล้ว")

# ตั้งค่าข้อมูลที่ได้รับจาก Telegram
# api_id = '23655938'  # แทนที่ด้วย api_id ของคุณ
# api_hash = '41aeef7ed4bf558e7e6e9751ffc87906'  # แทนที่ด้วย api_hash ของคุณ
# phone_number = '0628026006'  # หมายเลขโทรศัพท์ของคุณ

# ตั้งค่าข้อมูลที่ได้รับจาก Telegram
api_id = '24526330'  # แทนที่ด้วย api_id ของคุณ
api_hash = '7e6566f5cb575553cd0ddc18f5f3bb1a'  # แทนที่ด้วย api_hash ของคุณ
phone_number = '0841304874'  # หมายเลขโทรศัพท์ของคุณ

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    # เริ่มต้นเซสชันของไคลเอนต์
    await client.start(phone=phone_number)
    print("เข้าสู่ระบบเรียบร้อยในชื่อ:", await client.get_me())

    # ตรวจสอบกลุ่มและช่องสนทนาที่มีอยู่
    dialogs = await client.get_dialogs()
    
    print("กลุ่มและช่องสนทนาที่คุณเข้าร่วม:")
    groups_info = []
    for dialog in dialogs:
        if dialog.is_group or dialog.is_channel:
            # ดึงข้อมูลกลุ่ม
            entity = await client.get_entity(dialog.id)
            date_joined = entity.date  # วันที่เข้าร่วมกลุ่ม
            participants = await client.get_participants(dialog.id)  # ดึงข้อมูลสมาชิก
            member_count = len(participants)  # นับจำนวนสมาชิก
            
            # ตรวจสอบและสร้างลิงก์เชิญใหม่ถ้าไม่มี
            if entity.username:
                invite_link = f"https://t.me/{entity.username}"
            elif hasattr(entity, 'invite_link') and entity.invite_link:
                invite_link = entity.invite_link
            else:
                result = await client(functions.messages.ExportChatInviteRequest(peer=entity))
                invite_link = result.link
                print(f"สร้างลิงก์เชิญใหม่สำหรับกลุ่ม: {dialog.name}")
            
            # เพิ่มข้อมูลกลุ่ม
            groups_info.append((dialog.name, dialog.id, date_joined, member_count, invite_link))
            print(f"- {dialog.name} (ID: {dialog.id}, วันที่เข้าร่วม: {date_joined}, จำนวนสมาชิก: {member_count}, ลิงก์เชิญ: {invite_link})")

    # เตรียมข้อความที่จะส่งเกี่ยวกับข้อมูลกลุ่มและสมาชิก
    message = "กลุ่มที่คุณเข้าร่วมและข้อมูลสมาชิก:\n\n"
    for group_name, group_id, date_joined, member_count, invite_link in groups_info:
        message += f"━━━━━━━━━━━━━━━━━━━━━━━\n"
        message += f"📌 ชื่อกลุ่ม: {group_name}\n"
        message += f"📋 ID: {group_id}\n"
        message += f"⏰ วันที่เข้าร่วม: {date_joined.strftime('%Y-%m-%d %H:%M:%S')}\n"
        message += f"👥 จำนวนสมาชิก: {member_count}\n"
        message += f"🔗 ลิงก์เชิญ: {invite_link}\n"
        message += "━━━━━━━━━━━━━━━━━━━━━━━\n"

        # ดึงข้อมูลผู้เข้าร่วมและแสดงในคอนโซล
        participants = await client.get_participants(group_id)
        for participant in participants:
            username = participant.username if participant.username else "ไม่มีชื่อผู้ใช้"
            full_name = f"{participant.first_name} {participant.last_name}" if participant.first_name else "ไม่ทราบชื่อ"
            phone = participant.phone if participant.phone else "ไม่มีหมายเลขโทรศัพท์"
            
            # แสดงข้อมูลผู้เข้าร่วมในคอนโซล
            print(f"  - 👤 Username: {username}")
            print(f"  - 👥 ชื่อเต็ม: {full_name}")
            print(f"  - 📱 หมายเลขโทรศัพท์: {phone}")
            print(f"  - 🆔 ID: {participant.id}")
            print("-----------------------")
            
            # เพิ่มข้อมูลผู้เข้าร่วมในข้อความ
            message += f"  - 👤 Username: {username}\n"
            message += f"  - 👥 ชื่อเต็ม: {full_name}\n"
            message += f"  - 📱 หมายเลขโทรศัพท์: {phone}\n"
            message += f"  - 🆔 ID: {participant.id}\n"
            message += "-----------------------\n"
            
    # user_id ของผู้ใช้ที่ต้องการส่งข้อความ
    user_id = 6757863220  # แทนที่ด้วย user_id ของผู้ใช้ที่ต้องการส่งข้อความ

    # ส่งข้อความหาผู้ใช้
    await client.send_message(user_id, message)
    print(f"ข้อความกลุ่มและสมาชิกถูกส่งไปยังผู้ใช้ที่มี ID: {user_id}")

# เรียกใช้ client
with client:
    client.loop.run_until_complete(main())