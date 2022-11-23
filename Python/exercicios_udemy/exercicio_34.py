# Criando um código que verifica se um determinado item se encontra presente na lista.
# Aqui também aprendemos a driblar o problema do Case Sensitive do python nas caixas de input.

cores = ['amarelo', 'verde', 'azul', 'vermelho']    # Lista dos itens
cor_desejada = input('Qual cor você quer conferir? ')   # Aqui o usuário digita qual a cor

if cor_desejada.lower() in cores:   # O comando .lower() serve para corrigir o problema do usuário colocar tudo em maiúsculo.
    print('Essa cor está presente na lista!')
else:
    print('Cor indisponível.')
