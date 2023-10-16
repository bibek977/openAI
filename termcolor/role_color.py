from termcolor import colored

my_dict = [
    {
        'id' : 'human',
        'message' : "human beings are natural",
    },
    {
        'id' : 'Ai',
        'message' : "Ai are artificial"
    }
]

specific_color = {
    'human' : 'green',
    'Ai' : 'blue'
}

for i in my_dict:

    print(colored(f"{i['message']}",specific_color[i['id']]))