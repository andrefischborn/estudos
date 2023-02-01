'''
Usando FOR LOOP com IF e ELSE
'''

dados_compra = 'Compra Confirmada!'
compra_confirmada = True
for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
    break
else:
    print('Falha na compra!')
