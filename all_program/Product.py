from api_key import api_key
import openai
import json

openai.api_key = api_key

def get_product(num1,num2):
    return str(num1*num2)

def get_add(num1,num2):
    p = f"The result of {str(num1)} and {str(num2)} is :  {str(num1+num2)}"


def run_product():
    
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo-0613",
        messages = [
            {
                "role":"user",
                "content" : "What is the product of 4 and 9"
            },
        ],
        
        functions = [
            {
                "name" : "get_product",
                "description" : "find the multiply of 2 numbers",
                "parameters" : {
                    "type" : "object",
                    "properties" : {
                        "num1":{
                            "type":"integer",
                            "description" : "The first number, e.g. 1"
                        },
                        "num2":{
                            "type":"integer",
                            "description" : "The second number, e.g. 1"
                        },
                    },
                    "required" : ["num1","num2"]
                } 
            }
        ],

        function_call = "auto",
    )

    message = response["choices"][0]["message"]
    print(message)

    if message.get("function_call"):

        function_name = message["function_call"]["name"]
        arguments = json.loads(message["function_call"]["arguments"])

        num1 = arguments["num1"]
        num2 = arguments["num2"]

        function_response = get_product(num1,num2)

        second_response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo-0613",
            messages = [
                {"role":"user",
                 "content" : "What is the product of 4 and 9"},
                 message,
                 {
                     "role" : "function",
                     "name" : function_name,
                     "content" : function_response
                 }
            ]
        )

        return second_response
    
response = run_product()
data = response["choices"][0]["message"]["content"]
print(data)