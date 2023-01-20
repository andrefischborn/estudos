'''
Calculo de Indice de Massa Corporal

Menor que 18.5 - Magreza
Entre 18.5 e 24.9 - Normal
Entre 25.0 e 29.9 - Sobrepeso
Entre 30.0 e 39.9 - Obesidade
Maior que 40.0 - Obesidade Grave
'''

altura = float(input(f'Qual a altura? '))
peso = float(input(f'Qual o peso? '))
imc: float
imc = peso / (altura/100) ** 2
print(f'Seu IMC é: {imc:.1f}')

if imc < 18.5:
    print(f'Você está Magro')
elif imc >= 18.5 and imc < 25:
    print(f'Você está Normal')
elif imc >= 25 and imc < 30:
    print(f'Você está com Sobrepeso')
elif imc >= 30 and imc < 40:
    print(f'Você está com Obesidade')
else:
    print(f'Você está com Obesidade Grave')


# Os dados informados nessa calculadora não estão de acordo com os dados informados por profissional da saúde.
# Estes dados servem apenas para estudo de LÓGICA DE PROGRAMAÇÃO.