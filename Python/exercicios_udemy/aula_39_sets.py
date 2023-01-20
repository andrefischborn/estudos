'''
                                 Criando SET
 Similar a listas
 Não utiliza index
 Evita itens duplicados
'''
list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]
# Os itens 10 e 20 estão duplicados nessas listas acima.

num1 = set(list1)
num2 = set(list2)

print(f'Impressão de SET da Lista 1:')
print(num1) # O set vai ser impresso dentro de CHAVES {} e a ordem fica misturada,
            # Sem indexação. Não sendo possível imprimir uma determinada posição caso queira: Ex: print(num1[3]) - Dará erro.
print()

# A Barra reta "|" se chama UNION: Ela vai unir os dois sets e imprimir eles sem imprimir os duplicados várias vezes, apenas uma.
print(f'Impressão da união dos dois SET usando UNION:')
print(num1 | num2) 
print()

# Também temos o "Difference": Simbolo "-" - Imprime só o que os sets tem de diferente do primeiro em relação ao segundo.
print(f'Usando DIFFERENCE:')
print(num1 - num2)
print()

# Outro simbolo interessante é o SIMETRIC: Simbolo "^" - Ele retira os itens DUPLICADOS e não os imprime, diferente do UNION.
print(f'Usando SIMETRIC:')
print(num1 ^ num2)
print()

# Por ultimo temos o AND: Simbolo "&" - Ele imprime apenas os Duplicados.
print(f'Usando AND:')
print(num1 & num2)
print()
