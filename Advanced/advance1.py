import openai
from dotenv import load_dotenv
import os

import mysql.connector



load_dotenv()
openai.api_key = os.getenv('secret_key')

gpt_model = 'gpt-3.5-turbo-0613'

all_messages = []

system_message =  {
        'role':'system',
        'content' : 'You are a Blog Content Creator. Create a blog content from given topic or sentences. Blog content should be less than 250 words.'
    }

all_messages.append(system_message)

user_message = {
    'role' : 'user',
    'content':'iphone vs samsung'
}
all_messages.append(user_message)

response = openai.ChatCompletion.create(
    model = gpt_model,
    messages = all_messages,
    temperature = 0.6
)

blog_content = response['choices'][0]['message']['content']
print(blog_content)

if blog_content:
    image_messages = [
        {
            'role' : 'system',
            'content' : 'You are a content summerizer who summerize into 3 or 4 keywords words related to the content. You use the keywords and the topic of content and generates the perfect matching image for the content.'
        },
    ]

    content_message = {
        'role' : 'user',
        'content' : blog_content
    }

    image_messages.append(content_message)

    summary = openai.ChatCompletion.create(
        model = gpt_model,
        messages = image_messages,
        temperature = 0.6
    )

    image_summary = summary['choices'][0]['message']['content']
    print("=========================================================")
    print(image_summary)
    print("=========================================================")

    if image_summary:

        image_response = openai.Image.create(
            prompt = image_summary,
            # prompt = user_message['content'],
            n = 1,
            size = '256x256'
        )

        print(image_response)
        image_url =image_response['data'][0]['url']
        print(image_url)

    else:
        print("image summary time error")

else:
    print('blog content response time error')


try : 
    mydb = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'root',
    database = 'openAI'
    )

    print(mydb)
    mycursor = mydb.cursor()

    sql = "INSERT INTO blog (title, blog_desc ,image_summary,image_url) VALUES (%s,%s,%s,%s)"

    val = (user_message['content'],blog_content,image_summary,image_url)

    mycursor.execute(sql,val)

    mydb.commit()

    print(mycursor.rowcount,"rows inserted")

except Exception as e:
    print("==========================")
    print("not saved in database")
    print("==========================")

    print(e)