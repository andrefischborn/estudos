import datetime 
'''
             #Problema "duracao"
Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no
formato horas:minutos:segundos.
    Exemplo 1:
        Digite a duracao em segundos: 300
        0:5:0
    Exemplo 2:
        Digite a duracao em segundos: 12506
        3:28:26
    Exemplo 3:
        Digite a duracao em segundos: 140811
        39:6:51 
'''
n = int(input('Qual o tempo em segundos? '))

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 
      
print(convert(n)) 

# Usando DIVMOD

def convert(seconds): 
    min, sec = divmod(seconds, 60) 
    hour, min = divmod(min, 60) 
    return "%d:%02d:%02d" % (hour, min, sec) 
      
print(convert(n))

# outro modo de fazer usando a LIB datetime:
 
def convert(n): 
    return str(datetime.timedelta(seconds = n)) 
      
print(convert(n)) 