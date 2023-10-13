import openai
from dotenv import load_dotenv
import os
import pandas as pd
import tiktoken

from wiki_baloon import wiki_baloon

load_dotenv()
openai.api_key = os.getenv("secret_key")

gpt_model = 'gpt-3.5-turbo-0613'
all_messages = [

]

system_messages = {
    'role' : 'system',
    'content' : 'you are a helpful assistant. you gather knowledge about football and answer back to user.'
}
all_messages.append(system_messages)

qeury = "Which player won the balloond'or in 2022?"
all_messages.append({
    'role' : 'user',
    'content' : qeury
})

response = openai.ChatCompletion.create(
    model = gpt_model,
    messages = all_messages,
    temperature = 0
)

# print(response)
response_data = response['choices'][0]['message']['content']
print(response_data)

user_input = input("Enter any query: ")

second_query = f"""
Use the following article below on 2022 baloond'or winner lists to answer the question.
If you don't found the answer , write "I don't know bibek, sorry"
'''
Article
<>
{wiki_baloon}
<>
'''
{user_input}
"""

second_response = openai.ChatCompletion.create(
    model = gpt_model,
    messages = [
        {
            'role' : 'system',
            'content' : 'you are a helpful assistant. you gather knowledge about football and answer back to user.'
        },
        {
            'role' : 'user',
            'content' : second_query
        }
    ],
    temperature = 0

)

second_response_data = second_response['choices'][0]['message']['content']
print(second_response_data)