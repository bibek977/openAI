import openai

from api_key import api_key
openai.api_key = api_key

messages = [
    {'role' : 'system','content':'You are a kind helpful assistant'},
]

run = True
while run:
    message = input("Bibek : ")
    if message == "stop":
        run = False

    else:
        messages.append(
            {'role' : 'user','content':message},
        )
        chat = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo',
            messages = messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGpt: {reply}")
    messages.append(
        {'role':'assistant','content':reply},
    )