'''
    Problema "aumento" (adaptado de URI 1048)
Uma empresa vai conceder um aumento percentual de
salário aos seus funcionários dependendo de quanto
cada pessoa ganha, conforme tabela ao lado. Fazer um
programa para ler o salário de uma pessoa, daí mostrar
qual o novo salário desta pessoa depois do aumento,
quanto foi o aumento e qual foi a porcentagem de
aumento.
                            Salário atual                           Aumento
                            Até R$ 1000.00                          20%
                            Acima de R$ 1000.00 até R$ 3000.00      15%
                            Acima de R$ 3000.00 até R$ 8000.00      10%
                            Acima de R$ 8000.00                     5%
    Exemplo 1:
        Digite o salario da pessoa: 2500.00
        Novo salario = R$ 2875.00
        Aumento = R$ 375.00
        Porcentagem = 15 %
    Exemplo 2:
        Digite o salario da pessoa: 8000.00
        Novo salario = R$ 8800.00
        Aumento = R$ 800.00
        Porcentagem = 10 %
'''
salario = float(input('Qual o salário da pessoa? '))

if salario <= 1000.00:
    x = 0.20
    porcentagem = '20%'

if (salario > 1000.00) and (salario <= 3000.00):
    x = 0.15
    porcentagem = '15%'

if (salario > 3000) and (salario <= 8000):
    x = 0.10
    porcentagem = '10%'

if salario > 8000:
    x = 0.05
    porcentagem = '5%'

diferenca = salario * x
novo_salario = salario + diferenca
aumento = novo_salario - salario

print(f'Novo salário: R$ %.2f' % (novo_salario))
print(f'Aumento de: %.2f' % (aumento))
print(f'Porcentagem: {porcentagem}')