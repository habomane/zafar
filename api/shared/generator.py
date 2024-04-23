import randomname
import random

def generate_username():
    name = randomname.get_name().replace('-', '_')
    number = int(random.random() * 200000)
    return name + str(number)

name = generate_username()
print(name)