import random
import secrets
import string
chars = string.ascii_letters + string.punctuation + string.digits
password = ''.join(secrets.choice(chars)
for _ in range(int(input('enter the range'))))
print(password)
