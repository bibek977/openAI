import openai
import requests
import json

from api_key import api_key
openai.api_key = api_key

url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type":"application/json",
    "Authorization":f"Bearer {openai.api_key}"
}

messages = [
            {
        'role':'system',
        'content':'You will have to answer the name of the person, his/her net worth and give the location where he lives'
    },
            {
        "role" : "user",
        "content" : "Who is the richest movie actor,actress and movie director in the world right now?"
    },
    ]
payload = {
    "model" : 'gpt-3.5-turbo',
    "messages": messages,
    "temperature":0,
    "top_p" : 1.0,
    "n" : 1,
    "stream":False,
    "presence_penalty":0,
    "frequency_penalty":0
}

response = requests.post(url=url,headers=headers,json=payload,stream=False)

content_data = response.content
print(content_data)
content_decode = content_data.decode('utf-8')
print(content_decode)


with open("Movies.json",'w') as f:
    f.write(content_decode)