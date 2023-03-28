# Try, except, else e finaly

# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')

except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print('Alguma variável não foi definida')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print(f'{error.__class__.__name__}')
except Exception:  # Exception classe superior de erros.
    print('ERRO desconhecido')


print('continuar')