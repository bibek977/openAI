from collections import defaultdict
from termcolor import colored

d = defaultdict(int)

list_data = [9,1,5,5,5,9,1,9,5,1,9]
list_data_2 = [9,1,5,5,5,3,1,9,5,1,4]

for i in list_data:
    d[i] += 1

for i in list_data_2:
    d[i] += 1


print(d)