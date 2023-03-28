# raise - lança exeções

# print(123)
# raise ValueError('Deu arro.')
# print(456)

# def divide(n, d):
#     try:
#         return n / d
#     except ZeroDivisionError:
#         # return n
#         print('Valor adicionada aos erros')
#         raise


# print(divide(8, 0))

def nao_aceito_zero(*d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True


def deve_ser_int_float(n):
    if not isinstance(n, (int, float)):
        raise TypeError(
            f'{n}, deve ser int ou float.'
        )
    return True


def divide(n, d):  # Da maneira que a função foi nomeada, ela idealmente não deve tratar os erros.

    deve_ser_int_float(n)

    deve_ser_int_float(d)

    nao_aceito_zero(d)
  
    return n / d

print(divide(8, 0))
