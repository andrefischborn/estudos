'''
            # Problema "consumo"
Fazer um programa para ler a distância total (em km) percorrida por um carro, bem como o total de
combustível gasto por este carro ao percorrer tal distância. Seu programa deve mostrar o consumo
médio do carro, com três casas decimais.
    Exemplo 1:
        Distancia percorrida: 500
        Combustível gasto: 38.5
        Consumo medio = 12.987
    Exemplo 2:
        Distancia percorrida: 1108
        Combustível gasto: 71.4
        Consumo medio = 15.518 
'''
distancia = int(input(f'Qual a distância percorrida? '))
combustivel_gasto = float(input('Quanto de combustível foi gasto? '))
consumo_medio = distancia /  combustivel_gasto

print(f'O consumo médio de combustível foi: {consumo_medio:.3f}')