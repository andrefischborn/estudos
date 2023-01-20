# os vetores na linguagem python são as listas ou tuplas.
# São dados indexados, podendo ser homogêneos.

# Exemplo:

N = int(input('Quantos números você quer listar? '))
vet: [float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input('Digite um número: '))

print()
print('NÚMEROS DIGITADOS:')
for i in range (0, N):
    print(f'{vet[i]:.1f}')
