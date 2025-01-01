import asyncio
import aiohttp

async def request_email_verification(session, email, service, num_attempts):
    verification_url = f"https://www.{service}.com/verifyemail?email={email}"

    for _ in range(num_attempts):
        async with session.get(verification_url) as response:
            if response.status == 200:
                return f"สำเร็จ: ร้องขอยืนยันทางอีเมลจาก {service} เรียบร้อย"
    
    return f"เกิดข้อผิดพลาด: ไม่สามารถร้องขอยืนยันทางอีเมลจาก {service} ได้"

async def main():
    email = input("กรุณาใส่ที่อยู่อีเมล: ")
    num_attempts = int(input("กรุณาใส่จำนวนครั้งที่ต้องการทดสอบ: "))

    services = ["google", "facebook", "twitter", "microsoft"]

    async with aiohttp.ClientSession() as session:
        tasks = [request_email_verification(session, email, service, num_attempts) for service in services]
        results = await asyncio.gather(*tasks)

        for result in results:
            print(result)

if __name__ == "__main__":
    asyncio.run(main())