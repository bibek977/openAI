from termcolor import colored,cprint

# text = colored("termcolor is used to color terminal", "red")

text = colored("termcolor is used to color terminal",
               "red",
               "on_yellow")
print(text)

cprint("cprint to color print terminal",
       "yellow",
       "on_green")

cprint("with attribute", 
       'white',
       attrs=['bold'])

