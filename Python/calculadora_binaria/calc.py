
print(f'Escolha qual tipo de valor você quer converter:')
print(f'(1) - Para converter Decimal em Binário')
print(f'(2) - Para converter Binário em Decimal')
escolha = int(input(f'Digite 1 ou 2: '))

while escolha >= 3:
    print(f'Escolha invalida. Tente novamente.')
    print(f'(1) - Para converter Decimal em Binário')
    print(f'(2) - Para converter Binário em Decimal')
    escolha = int(input(f'Digite 1 ou 2: '))

if escolha == 1:
    dividendo = int(input("Digite um numero DECIMAL para ser convertido em BINÁRIO: "))
    numero_digitado = dividendo
    quociente = 1
    lista = []

    while quociente >= 1:
        resto = dividendo%2
        lista.insert(0,resto)
        quociente = dividendo // 2
        dividendo = quociente

    binario = ''.join([str(item) for item in lista])
    print(f'O Número {numero_digitado} quando convertido em binário é {binario}')

if escolha == 2:
    binario = int(input('Digite o numero BINÁRIO para ser convertido em DECIMAL: '))
    n = len(str(binario))
    valor_digitado = binario
    decimal = 0
    i = 0

    while n >= 0:
        resto = binario % 10
        decimal = decimal + (resto * (2**i))
        n = n -1
        i = i + 1
        binario = binario // 10
    print(f'O Número {valor_digitado} quando convertido para decimal é {decimal}.')
