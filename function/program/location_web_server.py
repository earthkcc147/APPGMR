
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import time

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
        print(f"ที่อยู่: {data.get('latitude')},{data.get('longitude')}")
       # print(f"User-Agent: {data.get('userAgent')}")
        self.send_response(200)
        self.end_headers()
       # time.sleep(10)

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 5000), RequestHandler)
    print("มึงเอาลิงค์นี้ไปวางกูเกิ้ล http://127.0.0.1:5000")
    server.serve_forever()


