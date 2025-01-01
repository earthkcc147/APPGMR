pkg install imagemagick
pip install Wand


from wand.image import Image

# กำหนดค่าดีฟอลต์
default_input_file = 'input.jpg'
default_output_file = 'output.png'
default_width = 800
default_height = 600
default_rotate_angle = 90
default_output_format = 'png'

# รับค่าจากผู้ใช้หรือใช้ค่าดีฟอลต์
input_file = input(f"กรุณาระบุชื่อไฟล์ภาพ (กด Enter เพื่อใช้ค่าเดิม: {default_input_file}): ") or default_input_file
output_file = input(f"กรุณาระบุชื่อไฟล์ผลลัพธ์ (กด Enter เพื่อใช้ค่าเดิม: {default_output_file}): ") or default_output_file

# รับขนาดและมุมหมุนจากผู้ใช้
try:
    width_input = input(f"กรุณากรอกความกว้างใหม่ของภาพ (กด Enter เพื่อใช้ค่าเดิม: {default_width}): ")
    width = int(width_input) if width_input else default_width
    
    height_input = input(f"กรุณากรอกความสูงใหม่ของภาพ (กด Enter เพื่อใช้ค่าเดิม: {default_height}): ")
    height = int(height_input) if height_input else default_height
    
    rotate_angle_input = input(f"กรุณากรอกมุมหมุนภาพ (กด Enter เพื่อใช้ค่าเดิม: {default_rotate_angle}): ")
    rotate_angle = int(rotate_angle_input) if rotate_angle_input else default_rotate_angle
except ValueError:
    print("กรุณากรอกค่าตัวเลขที่ถูกต้องสำหรับขนาดและมุม")
    exit()

output_format = input(f"กรุณากรอกฟอร์แมตภาพที่ต้องการ (กด Enter เพื่อใช้ค่าเดิม: {default_output_format}): ") or default_output_format

# เปิดไฟล์ภาพ
with Image(filename=input_file) as img:
    # แสดงข้อมูลเบื้องต้นของภาพ
    print(f'Width: {img.width}')
    print(f'Height: {img.height}')
    print(f'Format: {img.format}')

    # ปรับขนาดภาพ (resize)
    img.resize(width, height)

    # เปลี่ยนฟอร์แมตของภาพจากไฟล์ที่ผู้ใช้ระบุ
    img.format = output_format
    
    # บันทึกภาพใหม่
    img.save(filename=output_file)
    
    # หมุนภาพตามมุมที่ผู้ใช้ระบุ
    img.rotate(rotate_angle)
    
    # บันทึกภาพที่หมุนแล้ว
    rotated_output_file = f"rotated_{output_file}"
    img.save(filename=rotated_output_file)

    print(f"ภาพถูกบันทึกเป็น {output_file} และ {rotated_output_file}")