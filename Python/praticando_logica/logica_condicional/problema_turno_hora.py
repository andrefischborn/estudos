'''
Brincando com IF/ELSE/ELIF
'''
hora = int(input('Que horas são? '))


def turno():
    if ((hora >= 12) and (hora <= 18)):
        print(f'Boa tarde!')
    elif ((hora >= 19) and (hora <= 23)):
        print('Boa noite!')
    elif ((hora >= 0) and (hora <= 5)):
        print('Madrugada!')
    elif (hora <= 11): 
        print(f'Bom dia!')
    else:
        print('Horário Inválido! (máximo 23)')

turno()