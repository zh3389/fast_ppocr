import requests

url = 'http://localhost:9001/ocr'
img_path = 'assets/1.png'

with open(img_path, 'rb') as f:
    file_dict = {'image_file': (img_path, f, 'image/png')}
    response = requests.post(url, files=file_dict, timeout=60)

print(response.json())
