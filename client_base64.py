import base64
import requests

url = 'http://localhost:9001/ocr'
img_path = 'assets/1.png'

with open(img_path, 'rb') as fa:
    img_str = base64.b64encode(fa.read())

payload = {'image_data': img_str}
response = requests.post(url, data=payload)

print(response.json())
