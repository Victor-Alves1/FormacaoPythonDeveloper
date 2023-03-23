import random
import string

password_size = 16
chars = string.ascii_letters + string.digits + "!@#$%&"
aleatorio = random.SystemRandom()

print(''.join(aleatorio.choice(chars) for i in range(password_size)))