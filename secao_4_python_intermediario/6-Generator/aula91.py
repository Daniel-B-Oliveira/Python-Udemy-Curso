# Introdução a generator functions em Python
# generator = (n for n in range(1000))

def generator(n=0, maximum=10):
    while True:
        yield n

        if n == maximum:
            return

        n += 1

gen = generator(maximum=10000)

for n in gen:
    print(n)