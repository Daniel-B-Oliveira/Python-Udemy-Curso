"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'Daniel Barreto'
# Troca de maneira complexa o valor [3]: 
outra_variavel = string = f'{string[:3]}ABC{string[4:]}'
# string[3] = 'ABC'
print(outra_variavel)
