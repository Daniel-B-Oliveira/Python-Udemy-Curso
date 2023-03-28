# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def creat_function(func):
    def inter(*args, **kwargs):

        for arg in args:
            is_string(arg)
    
        result = func(*args, **kwargs)

        return result 
    return inter



@creat_function  # esta função "some" e vai para a creat_function
def invert_string(string):  # !!! esta função vira a interna !!!
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Param need to be a string')

# invert_string_check_param = creat_function(invert_string)
# inverted = invert_string_check_param('123')
# print(inverted)

inverted = invert_string('123')
print(inverted)