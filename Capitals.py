import openai

from api_key import api_key
openai.api_key = api_key

messages = [
    {'role':'system','content':
     '''You will be provided the name of the country and you have to find the capital of the country.
        Just tell me the word of capital.
        If given input from user is not country name you can tell the given name is not matched with any country name.
        If the given name is matched with any city tell them the given name is a name of city.
        If the given name is capital of any country then provide the name of the country instead.
     '''},
]

run = True
while run:

    message = input("Bibek : ")

    if message:

        if message == "stop":
            run = False

        else:
            messages.append(
                {'role':'user','content':message},
            )

            chat = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages = messages
            )

        reply = chat.choices[0].message.content
        print(f"ChatGPT : {reply}")

        messages.append(
            {'role':'assistant','content':reply},
        )