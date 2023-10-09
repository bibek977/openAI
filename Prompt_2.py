import jinja2
import openai
from api_key import api_key

openai.api_key = api_key

with open("Prompt_2.jinja2","r") as f:
    prompt = jinja2.Template(f.read())

labels = [
    {'label':0,"description":"negative"},
    {'label':1,"description":"neutral"},
    {'label':2,"description":"positive"},
]

examples = [
    {'text' : "he is a good man" , 'label':2},
    {'text' : "he is a terrible man" , 'label':0},
]

# text = "I love playing football"
text = "I am playing football"

result = prompt.render(
    labels = labels,
    examples = examples,
    text = text
)
print(result)

response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo-0613',
    messages = [
        {'role' : 'system', 'content' : 'you are a helpful assistant'},
        {'role' : 'user','content' : result}
    ]
)

print(response['choices'][0]['message']['content'])