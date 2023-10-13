import openai
from dotenv import load_dotenv
import os
import json
import pandas as pd
from pprint import pprint

load_dotenv()
openai.api_key = os.getenv('secret_key')

gpt_model = 'gpt-3.5-turbo-0613'

movies_df = pd.read_csv("Advanced/movies.csv")

train = []

system_message = 'You are a helpful assistant. You are to extract data of Film from each of the given Film provided.'

def create_user_message(row):
    message = f""" Film : {row['Film']} \n  Genre : {row['Genre']} \n Worldwide Gross : 
                """
    return message
    
def get_movie_data (row):
    messages = []
    messages.append({
        'role' : 'system',
        'content' : system_message
    })

    user_message = create_user_message(row)
    messages.append({
        'role' : 'user',
        'content' : user_message
    })

    messages.append({
        'role' : 'assistant',
        'content' : f"{row['Worldwide Gross']}"
    })

    return {"messages" : messages}


pprint(get_movie_data(movies_df.iloc[0]))

training_df = movies_df.loc[0:25]
training_data = training_df.apply(get_movie_data, axis=1).tolist()

for example in training_data[:5]:
    pprint(example)

validation_df = movies_df.loc[25:50]
validation_data = validation_df.apply(get_movie_data,axis=1).tolist()
for i in validation_data[:5]:
    pprint(i)


def write_jsonFile(data_list : list, filename:str):
    with open(filename,"w") as f:
        for i in data_list:
            json_data = json.dumps(i) + "\n"
            f.write(json_data)

training_filename = "Advanced/Files/training_data.jsonl"
write_jsonFile(training_data,training_filename)

validating_filename = "Advanced/Files/validating_data.jsonl"
write_jsonFile(validation_data,validating_filename)

# try:
#     training_response = openai.File.create(
#         file=open(training_filename,"rb"),
#         purpose='fine-tune'
#     )
#     training_response_id = training_response['id']
#     print(training_response_id)

# except Exception as e:
#     print(e)

# try:
#     validating_response = openai.File.create(
#         file=open(validating_filename,"rb"),
#         purpose='fine-tune'
#     )
#     validating_response_id = validating_response['id']
#     print(validating_response_id)

# except Exception as e:
#     print(e)

try:
    response = openai.FineTuningJob.delete(
        training_file = "file-TMtGVCaciWQEYckAdTfQNqZt",
        validation_file = "file-dLTGaRRgATuKZ1gugMi58F9W",
        model = 'gpt-3.5-turbo-0613',
        suffix = 'movies-budget'
    )
    job_id = response['id']
    print(job_id)
    print(response['status'])

except Exception as e:
     print(e)