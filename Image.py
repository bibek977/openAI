import openai
from api_key import api_key

openai.api_key = api_key

img_data = openai.Image.create(
    prompt = "luffy and zoro from one piece anime",
    n = 1,
    size = "256x256"
)

img_url = img_data['data'][0]['url']

print(img_url)

image_1 = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-sLSBU95bo4418lWSggHWfhEC/user-NqCKTnEFPY7ukmBAWWyL5Ejj/img-Nrrl5flsoFwE4aoDtwTmS9lA.png?st=2023-10-04T09%3A04%3A38Z&se=2023-10-04T11%3A04%3A38Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-10-04T01%3A42%3A09Z&ske=2023-10-05T01%3A42%3A09Z&sks=b&skv=2021-08-06&sig=ecIZAjFQu%2BGcIGVZFVeSL7DJv5LOG7gM5/wZ1q/Zw3I%3D"

image_2 = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-sLSBU95bo4418lWSggHWfhEC/user-NqCKTnEFPY7ukmBAWWyL5Ejj/img-mhNCKg5zCPtEi2gjZUF3Av1U.png?st=2023-10-04T09%3A08%3A19Z&se=2023-10-04T11%3A08%3A19Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-10-04T01%3A39%3A35Z&ske=2023-10-05T01%3A39%3A35Z&sks=b&skv=2021-08-06&sig=HDZxN0XVUVRZ/lRCenNJPPM6PNpOeFgENyQinQMGloc%3D"

image_3 = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-sLSBU95bo4418lWSggHWfhEC/user-NqCKTnEFPY7ukmBAWWyL5Ejj/img-v8pjPRieGZJYKXi4LSrKTJBj.png?st=2023-10-04T09%3A09%3A26Z&se=2023-10-04T11%3A09%3A26Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-10-04T01%3A39%3A30Z&ske=2023-10-05T01%3A39%3A30Z&sks=b&skv=2021-08-06&sig=Z68HFg5p195I4s8wmlpGfhCmdkGFyIWI2mTuZJXB1I0%3D"

image_4 = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-sLSBU95bo4418lWSggHWfhEC/user-NqCKTnEFPY7ukmBAWWyL5Ejj/img-RhyxMkt6JHsqZQEHPZBFQ57G.png?st=2023-10-04T09%3A10%3A28Z&se=2023-10-04T11%3A10%3A28Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-10-04T01%3A40%3A14Z&ske=2023-10-05T01%3A40%3A14Z&sks=b&skv=2021-08-06&sig=ViWB9W3dPwTOji5tEVfkc7xe9K%2BF3MrpxJ%2B59FfmkN0%3D"