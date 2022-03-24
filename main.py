from datetime import datetime

now = datetime.now() # Data e hora atual

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)

import datetime
ano= 2022       #formato AAAA
mes=  3        #usar numeros
dia= 25

datapadrao = datetime.date(ano, mes, dia)
hoje = datetime.date.today()

if datapadrao > hoje:
    delta = datapadrao - hoje

elif datapadrao <= hoje:
    delta = hoje - datapadrao

print (delta.days)
if delta.days>=28:
    print('atualizar')    #vai precisar de else if com integração de banco de dados

else:
    quit()
