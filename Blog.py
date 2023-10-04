import openai
from api_key import api_key

openai.api_key = api_key

messages = [
    {
        'role' : 'system',
        'content' : '''  Create a Blog post on the topic which will be given by user.
                        Tags will be also given so use the tags to relate the blog content.
                        Divide the content in some part maximum 4 or 5 parts with words limits 150 to 200 words in each content.
                        The content should be as follows:
                        1. History or Definations
                        2. Imporatnce or Impacts
                        3.Current Situations of given topics related fiels
                        4. Some examples to relate the content with real world
                        5. Conclusion
                        '''
    },
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