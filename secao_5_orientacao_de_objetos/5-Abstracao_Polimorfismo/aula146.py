# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
    ...



class AnotherError(Exception):
    ...


def my_raise():
    exception_ = MyError('a',' b', 'c')
    exception_.add_note('Bom dia amigo, tome aqui um errinho')
    raise exception_

try:
    my_raise()
except (MyError,ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    exception_  = AnotherError('Vou lançar de novo')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('...mais um erro, no caso')
    raise exception_ from error
