import openai
from dotenv import load_dotenv
import os


load_dotenv()
openai.api_key = os.getenv('secret_key')

gpt_model = 'gpt-3.5-turbo-0613'

all_message = [

]

system_message = {
    'role' : 'system',
    'content' : 'You are a currency converter. Take the input number as U.S. doller so convert into Nepali rupees?'
}
all_message.append(system_message)

user_message = {
    'role' : 'user',
    # 'content' : '1 U.S. doller equals to how much nepali rupees?'
    'content' : '399'
}
all_message.append(user_message)


def get_currency(n,value):
    return n*value

response = openai.ChatCompletion.create(
    model = gpt_model,
    messages = all_message,
    temperature = 0.6   
)

response_data = response['choices'][0]['message']['content']
print(response_data)