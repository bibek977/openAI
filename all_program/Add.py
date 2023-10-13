import openai
from api_key import api_key
import json

openai.api_key = api_key

def get_addition(n,m):
    sub = n-m
    return str(sub)

def main():
    
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo-0613',
        messages = [
            {
                'role' : 'user',
                # 'content' : 'give me the capital city of nepal'
                'content' : 'What is sub of 2 and 9'
             },
        ],
        functions = [
            {
                'name' : 'get_addition',
                'description' : 'Adding 2 numbers',
                'parameters' : {
                    'type' : 'object',
                    'properties' : {
                        "n" : {
                            "type": "integer",
                            "description" :"first number, e.g. 3"
                        },
                        "m" : {
                            "type" : "integer",
                            "description" : "second number, e.g. 4"
                        }
                    },
                    "required" : ["n","m"]
                }
            }
        ],
        function_call = "auto",
    )

    message = response['choices'][0]['message']
    print(message)

    if message.get("function_call"):

        function_name = message['function_call']['name']
        arguments = json.loads(message['function_call']['arguments'])

        n = arguments['n']
        m = arguments['m']

        function_response = get_addition(n,m)

        second_response = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo-0613',
            messages = [
                {
                    'role' : 'user',
                    'content' : "What is sub of 2 and 9"
                },
                message,
                {
                    'role' : 'function',
                    'name' : function_name,
                    'content' : function_response
                }
            ],
        )

        return second_response
    
sub = main()
if sub:
    print(sub['choices'][0]['message']['content'])
else:
    print("sub is not defined")