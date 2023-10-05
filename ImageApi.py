from api_key import api_key
import openai
import requests
openai.api_key = api_key
img_data = openai.Image.create_edit(
  image=open("skyImg.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="A big dragon flying in sky",
  n=2,
  size="1024x1024"
)

img_url = img_data['data'][0]['url']

print(img_url)

response = requests.get(img_url)

if response.status_code == 200:


    with open("images/newImage."+"png",'wb') as f:
        f.write(response.content)
        print("image download successful")

else:
    print("Access denied to download image")
