# if / elif      / else
# se / se não se / se não

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1 == True:
    print('Este é o código da condição 1')
elif condicao2 == True:
    print('Este é o código do condição 2')
elif condicao3 == True:
    print('Este é o código do condição  3')
elif condicao4 == True:
    print('Este é o código do condição  4')

else:  # else sempre o último
    print('Nenhuma condição foi satisfeita')

if 10 == 10:
    print('Outro if (10==10)')

print('Fora do if')
