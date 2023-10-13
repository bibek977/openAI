import openai
from api_key import api_key
import requests

openai.api_key = api_key

img_data = openai.Image.create(
    prompt = "Movie",
    n = 1,
    size = "256x256"
)

img_url = img_data['data'][0]['url']

print(img_url)

response = requests.get(img_url)

if response.status_code == 200:


    with open("images/moviews."+"png",'wb') as f:
        f.write(response.content)
        print("image download successful")

else:
    print("Access denied to download image")