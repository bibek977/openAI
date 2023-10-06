import openai
from api_key import api_key
import requests
from tenacity import retry,wait_random_exponential,stop_after_attempt
from termcolor import colored

new_model = 'gpt-3.5-turbo'

openai.api_key = api_key

@retry(wait=wait_random_exponential(min=1,max=40),stop=stop_after_attempt(3))
def chat_request(messages,function=None,model=new_model):
    headers = {
        "Content-Type" : "application/json",
        "Authorization" : f"Bearer {openai.api_key}"
    }
    body = {
        'model' : model,
        'messages' : messages
    }
    if function is not None:
        body.update(
            {'function' : function}
            )
        
        # get_function = function
        # return get_function
        
    try:
        # response = requests.post( url="https://api.openai.com/v1/chat/completions",
        #     headers=headers,
        #     json=body
        # )
        # return response
    
        response = openai.ChatCompletion.create(
            model = model,
            messages = body,
            # function = get_function
        )
        return response

    except Exception as e:
        print(e)
        return e
    
class Chat:

    def __init__(self):
        self.chat_history = []

    def add_chat(self,role,content):
        message = {'role':role,"content":content}
        self.chat_history.append(message)

    def display_chat(self):
        role_to_color = {
            'system': 'red',
            'user' : 'green',
            'assistant':'blue',
            'function' : 'magneta'
        }

        for message in self.chat_history:
            print(
                colored(
                    f"{message['role']} : {message['content']} \n \n",
                    role_to_color[message["role"]],
                )
            )

function = [
    {
        'name' : 'get_current_weather',
        "description" : "Get the current weather in the given locaton",
        "parameters" : {
            "type" : "object",
            "properties":{
                "location" : {
                    "type" : "string",
                    "description" : "The city or district like Kathmandu, Pokhara, Hetuada",
                },
                "format" : {
                    "type" : "string",
                    "enum" : ["celcius","farenheit"],
                    "description" : "The temperature unit to use. Infer this from user location.",
                }
            }

        },
        "required" : ["location","format"],
    },
]

chat = Chat()

chat.add_chat("user","Tell me the weather of Birgunj today")

try:
    chat_response = chat_request(
        messages=chat.chat_history,
        function=function,
    )
    print(chat_response)
except Exception as e:
    print(e)