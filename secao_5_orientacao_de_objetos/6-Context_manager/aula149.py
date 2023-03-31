# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.

# ex: 
# with open('abcde', 'w', ) as arquivo:
#     ...

class My_Open:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self._file = None


    def __enter__(self):
        self._file = open(self.file_path, self.mode, encoding='utf8')
        return self._file
    
    def __exit__(self, class_exception, exception_, traceback_):
        self._file.close()
        # raise class_exception(*exception_.args).with_taceback(traceback_)

        # print(class_exception)
        # print(exception_)
        # print(traceback_)

        exception_.add_note('mInha nota')
        raise ConnectionError('Não deu para enviar')

        # return True



PATH = 'C:\\Users\\danie\\Documents\\curso_python\\udemy_python\\secao_5_orientacao_de_objetos\\6-dunder\\'
my_file_path = PATH + 'aula149.txt'

with My_Open(my_file_path, 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    file.write('Linha 4\n')
    file.write('Linha 5\n')
    print('with', file)

