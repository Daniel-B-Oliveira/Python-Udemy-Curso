# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome=}.')  # nome -> apenas valor; nome= -> variavel + valor

numero_1= (input('Digite um número: '))
numero_2 = (input('Digite outro número: '))

# int(input) não recomendado, crash o programa facilmente

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)



print(f'A soma dos numeros é: {int_numero_1+int_numero_2}')  # Não são números mas sim STR



