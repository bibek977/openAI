import json
import tiktoken
import numpy as np
from collections import defaultdict
from termcolor import colored

file_path = "fineTuning/file/data_sample.jsonl"

role_color = {
    'system' : 'green',
    'user' : 'white',
    'assistant' : 'red'
}

with open(file_path,'r') as f:
    data = [json.loads(line) for line in f]
    # print(data)
    for i in data:

        # print(colored(i,color=f['messages']['role']))
        # new_data = colored(i,role_color[i['messages'][0]['role']])
        new_data = colored(i,role_color[i['messages'][0]['role']])
        print(new_data)

        for n in new_data:
            # another_data = colored(i,role_color[i['messages'][0]['role']])  
            # if n['messages']:

            #     print(n['messages'])
            # print(type(n))
            if n.__contains__("role"):
                print("yes")
                

