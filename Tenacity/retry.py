from tenacity import *
import random

# @retry(stop=stop_after_attempt(2))
@retry
# @retry(stop=stop_after_delay(10))
# @retry(stop=(stop_after_attempt(2) | stop_after_delay(10) ))
# @retry(wait=wait_exponential(multiplier=1, min=4, max=10))
def even():
    num = random.randint(0,10)
    if num>1:
        # raise IOError("greater than five")
        print("greater than one")
        print(num)
        raise Exception
    else:
        print("success")
        print(num)

# even()

if __name__ == "__main__":
    print("name = main active")
    even()
    