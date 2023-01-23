'''
            # Problema "pagamento"
Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a
quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com
uma mensagem explicativa, conforme exemplo.
    Exemplo 1:
        Nome: Joao Silva
        Valor por hora: 50.00
        Horas trabalhadas: 60
        O pagamento para Joao Silva deve ser 3000.00
    Exemplo 2:
        Nome: Maria Dias
        Valor por hora: 60.00
        Horas trabalhadas: 100
        O pagamento para Maria Dias deve ser 6000.00 
'''

nome = input(f'Qual o nome do funcionário? ').title()
valor_hora = float(input(f'Qual o valor por hora de {nome}? '))
horas_trabalhadas = int(input(f'Quantas horas {nome} trabalhou? '))
pagamento = valor_hora * horas_trabalhadas

print(f'Nome: {nome}')
print(f'Valor por hora: R$ {valor_hora:.2f}')
print(f'Horas trabalhadas: {horas_trabalhadas} horas.')
print(f'O pagamento para {nome} deve ser R$ {pagamento:.2f}')
