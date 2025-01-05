import instaloader
import requests
import json

loader = instaloader.Instaloader()

username = input('กรุณากรอกชื่อผู้ใช้: ')
webhook_url = input('กรุณากรอก webhook: ')

profile = instaloader.Profile.from_username(loader.context, username)
for post in profile.get_posts():
    image_url = post.url
    
    payload = {
        'username': 'รูปภาพจาก Instagram!',
        'embeds': [
            {
                'title': f'ชื่อผู้ใช้ : {username}',
                'image': {
                    'url': image_url
                }
            }
        ]
    }
    
    response = requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})