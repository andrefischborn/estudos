'''
Operadores Lógicos
AND / OR / TRUE / FALSE

Operadores Ternários
<   >   =

'''
# Método longo:
idade = input('Qual a sua idade? ')
idade = int(idade)

if idade >= 16:
    print('Pode votar!')
else:
    print('Não pode votar!')
# #####################################################

# Método curto, otimizado:
resultado = 'Pode votar!' if idade >= 16 else 'Não pode votar!'
print(resultado)
