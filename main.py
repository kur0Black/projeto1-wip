from datetime import datetime

now = datetime.now() # Data e hora atual

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)

import datetime
ano= 2022       #formato AAAA
mes=  2        #usar numeros
dia= 12

datapadrao = datetime.date(ano, mes, dia)
hoje = datetime.date.today()

if datapadrao > hoje:
    delta = datapadrao - hoje

elif datapadrao <= hoje:
    delta = hoje - datapadrao

print (delta.days)
if delta.days>=28:
    print('Atualize seus dados.')    #vai precisar de else if com integração de banco de dados
    datapadrao = 0
    print(datapadrao)
else:
    quit() 
# Define a funcao
def calc_water_pkg(peso, need_agua):
    print("Voce precisa ingerir aproximadamente ",need_agua," Litros de agua. Peso: ",peso)

peso = 59   # Peso do usuario em KG
need_agua = 35 * peso # Calculo logico para quantidade de agua por Kilograma

calc_water_pkg(peso,need_agua) # Chama a funcao exportando os valores das variaveis
