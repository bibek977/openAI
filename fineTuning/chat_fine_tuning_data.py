import json
import tiktoken
import numpy as np
from collections import defaultdict
from termcolor import colored

file_path = "fineTuning/file/data_sample.jsonl"
role_color = {
    'system' : 'white',
    'user' : 'blue',
    'assistant' : 'green'
}
with open(file_path,'r') as f:
    data = [json.loads(line) for line in f]


# To check any content missing
format_errors = defaultdict(int)
for x in data:
    if not isinstance(x,dict):
        format_errors['data-type'] += 1
        continue

    messages = x.get("messages",None)
    if not messages:
        format_errors['no-message-list'] += 1
        continue

    for message in messages:
        if 'role' not in message and 'content' not in message:
            format_errors['missing-key'] +=1

        if any(r not in ("role", "content", "name", "function_call") for r in message):
            format_errors['format-unrecognized-key'] += 1

        if message.get('role',None) not in ("system","user","assistant"):
            format_errors['undefined-role'] += 1

        content = message.get("content",None)
        function_call = message.get("function_call",None)

        if (not content and not function_call) or not isinstance(content,str):
            format_errors['invalid-content'] += 1

    if not any(message.get('role',None) == 'assistant' for message in messages):
        format_errors['no-example-assistant'] += 1

if format_errors:
    print("Errors found : ")
    for k,v in format_errors.items():
        print(f"key : {k}\nvalue={v}")
else:
    print("Data is valid : ")


# To count token
encoding = tiktoken.get_encoding('cl100k_base')
def num_tokens_for_message(messages, tokens_per_message=3, tokens_per_name=1):
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key,value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3
    return num_tokens

def num_tokens_from_assistant(messages):
    num_tokens = 0
    for message in messages:
        if message['role'] == 'assistant':
            num_tokens += len(encoding.encode(message['content']))
    return num_tokens

def print_distrubution(value,name):
    print(f"\n\nDistribution of {name}")
    print(f"min-value : {min(value)} / max-value : {max(value)}")
    print(f"mean-value : {np.mean(value)} / median-value : {np.median(value)}")
    print(f"p5 : {np.quantile(value,0.1)} / p95 : {np.quantile(value,0.9)}")


# Data warning
n_missing_system = 0
n_missing_user = 0
n_messages = []
convo_lens = []
assistant_message_lens = []

for i in data:
    messages = i['messages']
    if not any(message['role'] == 'system' for message in messages):
        n_missing_system += 1
    if not any(message['role'] == 'user' for message in messages):
        n_missing_user += 1

    n_messages.append(len(messages))
    convo_lens.append(num_tokens_for_message(messages))
    assistant_message_lens.append(num_tokens_from_assistant(messages))

print("Num example missing system",n_missing_system)
print("Num example missing user",n_missing_user)

print_distrubution(n_messages,"num messages per example")
print_distrubution(convo_lens,"num total token per example")
print_distrubution(assistant_message_lens,"num assistant token per example")


# Cost Estimization
MAX_TOKENS_PER_EXAMPLE  = 4096
TARGET_EPOCHS = 3
MIN_TARGET_EXAMPLES = 100
MAX_TARGET_EXAMPLES = 25000
MIN_DEFAULT_EPOCHS = 1
MAX_DEFAULT_EPOCHS = 25

n_epochs = TARGET_EPOCHS
n_train_examples = len(data)
if n_train_examples * TARGET_EPOCHS < MIN_TARGET_EXAMPLES:
    n_epochs = min(MAX_DEFAULT_EPOCHS, MIN_TARGET_EXAMPLES // n_train_examples)
elif n_train_examples * TARGET_EPOCHS > MAX_TARGET_EXAMPLES:
    n_epochs = max(MIN_DEFAULT_EPOCHS, MAX_TARGET_EXAMPLES // n_train_examples)

n_billing_total_dataset = sum(min(MAX_TOKENS_PER_EXAMPLE,length) for length in convo_lens)
print(f"\n\nDataset has {n_billing_total_dataset} tokens that will be charged for during training")
print(f"By Default you will train for {n_epochs} epochs on dataset")
print(f"By Default you will charge for {n_epochs*n_billing_total_dataset} tokens")