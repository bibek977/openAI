import pathlib
import jinja2

path = pathlib.Path("Prompt_1.jinja2")
# print(str(path))

with path.open() as f:
    data = jinja2.Template(f.read())

show = data.render(
    world = "World"
)
print(show)

# check = '5'
check = True
if check:
    print(check)
else:
    print("not avaliable")