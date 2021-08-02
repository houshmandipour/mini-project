import string
import random

length = int(input("Enter password length: "))
chars = string.ascii_uppercase + string.ascii_lowercase + string.digits

print(''.join(random.choice(chars) for x in range(length)))
