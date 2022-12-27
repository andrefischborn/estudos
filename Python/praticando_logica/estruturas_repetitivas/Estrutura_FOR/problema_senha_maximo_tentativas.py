'''
    Problema "senha_fixa" (adaptado de URI 1114)
Escreva um programa que o usuário possa errar no máximo 5 vezes. Para cada leitura de
senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". Quando a senha
for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo
encerrado. Considere que a senha correta é o valor 2002.
    Exemplo:
        Digite a senha: 2312
        Senha Invalida! Tente novamente: 2010
        Senha Invalida! Tente novamente: 1022
        Senha Invalida! Tente novamente: 2002
        Acesso permitido!
'''

print('Digite a senha:')
tentativa = (input())
senha = '2002'
tent = 5
for i in range(tent):
    if tentativa != senha:
        if tent == 1:
            print(f'Senha Inválida! Tente novamente.')
            print(f'Você tem mais {tent} tentativa.')
            tent = tent -1
            tentativa = (input())
        if tent == 0:
            print(f'Sistema Bloqueado. Máximo de tentativas excedidas.')
            break
        else:
            print(f'Senha Inválida! Tente novamente.')
            print(f'Você tem mais {tent} tentativas.')
            tent = tent -1
            tentativa = (input())            
    elif tentativa == senha:
        print(f'Senha correta! Acesso permitido.')
        break

