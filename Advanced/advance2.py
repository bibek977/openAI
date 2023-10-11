import openai
from dotenv import load_dotenv
import os
import json
import pandas as pd
from pprint import pprint

load_dotenv()
openai.api_key = os.getenv('secret_key')

gpt_model = 'gpt-3.5-turbo-0613'

currency_df = pd.read_csv("Advanced/currency.csv")
print(currency_df.head())

training_data = []

all_message = [

]

system_message = {
    'role' : 'system',
    'content' : 'You are a helpful assistant. You have to extract the date according to country and the value of currency'
}

def create_user_message(row):
    return f""