'''
TRABALHANDO COM FUNCTIONS
A function é usada para diminuir a quantidade de códigos dentro de um programa.

DRY - Don`t Repet Yourself - Evitar os "Ctrl+C" e "Ctrl+V" que atolam o código de linhas repetidas.
Exemplo:
    print('Olá Mundo!')
    print('Seja bem vindo!')
    print('Olá Mundo!')
    print('Seja bem vindo!')            # ESSA REPETIÇÃO DEIXA O CÓDIGO HORRÍVEL
    print('Olá Mundo!')
    print('Seja bem vindo!')


'''

def boas_vindas():  # Criando a função.
    print('Olá Mundo!')
    print('Seja bem vindo!')
                                # Deixar sempre 2 linhas em branco - pep8
                                # Deixar sempre 2 linhas em branco - pep8
boas_vindas() # Agora é só digitar o nome da funcion que será executado aquelas linha acima.
boas_vindas() # Repeti 2 linhas de código com apenas uma palavra.
boas_vindas() # Repeti novamente.

#Usamos 3 linhas e economizamos outras 3.
