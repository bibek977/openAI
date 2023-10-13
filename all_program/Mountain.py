import openai
from api_key import api_key
import requests

openai.api_key = api_key

mountain_image = openai.Image.create_edit(
    image=open("images/ocean.png", "rb"),
    mask=open("images/boat.png", "rb"),
    prompt = " A big blue ocean and a big titanic ship",
    n = 2,
    size = "1024x1024"
)

image_url = mountain_image['data'][0]['url']
print(image_url)

response = requests.get(image_url)

if response.status_code == 200:


    with open("images/oceanWithBoat."+"png",'wb') as f:
        f.write(response.content)
        print("image download successful")

else:
    print("Access denied to download image")