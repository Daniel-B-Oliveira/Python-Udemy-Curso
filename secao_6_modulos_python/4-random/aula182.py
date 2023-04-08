# secrets gera números aleatórios e seguros

import secrets

import string as s
from secrets import SystemRandom as Sr

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=16)))
# print(''.join(Sr().choices(s.ascii_letters + s.digits, k=32)))

random = secrets.SystemRandom()  # Valores mais seguros

r_range = random.randrange(10, 20, 2)
print(r_range)

r_int = random.randint(10, 20)
print(r_int)

r_uniform = random.uniform(10, 20)
print(r_uniform)

nomes = ['Luiz', 'Maria', 'Helena', 'Joana']

random.shuffle(nomes)
print(nomes)

novos_nomes = random.sample(nomes, k=3)
print(nomes)
print(novos_nomes)

novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)

# # print(random.choice(nomes))