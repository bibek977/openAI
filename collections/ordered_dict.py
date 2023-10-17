from collections import OrderedDict
from termcolor import cprint

d = {}
d["C"] = 3
d["I"] = 9
d["B"] = 2
d["U"] = 21
d["Z"] = 26

for k,v in d.items():
    cprint(f"key = {k} \n value = {v}",'yellow')

cprint("\n Deleteing C : ","red","on_blue")
d.pop('C')

cprint("\n Adding again C",'blue','on_yellow')
d["C"] = 3

for k,v in d.items():
    cprint(f"key={k} \n value={v}",'blue')

od = OrderedDict()
od["C"] = 3
od["I"] = 9
od["B"] = 2
od["U"] = 21
od["Z"] = 26

for k,v in od.items():
    cprint(f"key = {k} \n value = {v}",'green')

cprint("\n Deleteing C : ","red","on_blue")
od.pop('C')

cprint("\n Adding again C",'blue','on_yellow')
od["C"] = 3

for k,v in od.items():
    cprint(f"key={k}\nvalue={v}",'green')