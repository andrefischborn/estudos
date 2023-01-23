frutas = ['Banana', 'Morango', 'Laranja', 'Bergamota']
frutas_preco = [10, 5, 8, 10]

verduras = ['Cebola', 'Alface', 'Pimentão']
verduras_preco = [4, 3, 18]

limpeza = ['Desodorante', 'Desinfetante']
limpeza_preco = [10, 8]

padaria = ['pao', 'cuca']
padaria_preco = [12, 15]

mercado_itens = [frutas+verduras+limpeza+padaria] # podemos unir as listas em uma variável
resultados = [ ]
resultados2 = [ ]

# Podemos criar um código que une 2 listas e coloca as ordens dos itens lado a lado, item 1 da lista 1 com o item 1 da lista 2.
def frutas2():
    for i in range(4):
        x=(frutas[i],frutas_preco[i])
        resultados.append(x)
    return(resultados)
    

def limpeza2():
    for i in range(2):
        x=(limpeza[i],limpeza_preco[i])
        resultados2.append(x)
    return(resultados2)


print(frutas2())
print()
print(limpeza2())



def type_unicode(text):
    import pyautogui
    import pyperclip
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


type_unicode("cd programação")