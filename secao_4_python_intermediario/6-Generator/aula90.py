
import sys

# Generator expression, Iterable e Iterators em Python
iterable = ['Eu', 'tenho', '__iter__',]
iterator = iter(iterable)
# print(next(iterator))

# lista = [n for n in range(10000000)]  # VALOR ABSURDO DE MEMÓRIA

# generator, não possui indice, não é navegável
generetator = (n for n in range(10000000))  # (n for n...) não é tupla, e sim generator

# print(sys.getsizeof (lista))
print(sys.getsizeof (generetator))

for n in generetator:
    print(n)
