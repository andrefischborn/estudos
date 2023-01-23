'''
Trabalhando com FOR LOOP - NUMEROS

Vamos supor que eu quero imprimir a sequência de 1 a 5:
    1
    2
    3
    4
    5
Poderiamos fazer:
    print('1')
    print('2')
    print('3')
    print('4')
    print('5')
Porém isso ficaria um absurdo para sequências longas, tipo 0 a 1000. 
Para isso usamos o "For in Range":

'''
for numero in range (1,6): # for variavel in range (numero_inicial,numero_final)
    print(numero)
for numero1 in range (1,1000): # para aparecer o número 1000, o correto seria colocar 1001. Lembre-se que o python conta a partir do 0!
    print(numero1)
