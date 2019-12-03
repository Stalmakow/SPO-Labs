#!/usr/bin/python3
import numpy as np
import re
used = open('gasUsed.txt', 'r')
price = open('gasPrice.txt', 'r')
contract = open('gasContracts.txt', 'r')

N=8945157

use = used.read().splitlines()
pric = price.read().splitlines()
contr = contract.read().splitlines()

GasUsed = []
Price = []
Contracts=[]

for i in use: 
	GasUsed.append(re.findall(r'\d+',i))
for i in pric:
	Price.append(re.findall(r'\d+',i))
for i in contr:
        Contracts.append(re.findall(r'\d+',i))
result = open('Result.txt', 'w')

Komission = []
OtnKomission = []
for i in range(1000):
	Komm = 0
	Contr=0
	for j in range(len(Price[i])):
		Komm += int(Price[i][j])*int(GasUsed[i][j])/(10**18)
		if Contracts[i][j]!=0:
			Contr+=1
	Komission.append(Komm)
	OtnKomission.append(Komm*100/(Komm+2))
	result.write(str(i+N) + ',' + str(Komm) + ',' + str(Komm*100/(Komm+2)) + ',' + str(Contr) + '\n')  

result.close()

import matplotlib.pyplot as plt
import collections as colct

countOtn=colct.Counter(OtnKomission)
countKomm=colct.Counter(Komission)
print(countOtn)
print(countKomm)

plt.subplot(1,2,1)
plt.scatter(countOtn.keys(),countOtn.values(),color='blue', s=7)
plt.title('График количества блоков с определенным процентом комиссии')
plt.xlabel('Комиссия %')
plt.ylabel('Кол-во блоков')

plt.subplot(1,2,2)
plt.scatter(countKomm.keys(),countKomm.values(),color='red', s=7)
plt.title('График количества блоков с определеннoй комиссиeй')
plt.xlabel('Комиссия ')
plt.ylabel('Кол-во блоков')

plt.show()


import statistics 
print('Абсолютное значение комиссии')
print('Медиана '+str(statistics.median(Komission)))
print('Размах '+str( max(Komission) - min(Komission)))
print('Среднее значение '+str(statistics.mean(Komission)))
print('Дисперсия '+str(statistics.variance(Komission)))
print('Отклонение '+str(statistics.stdev(Komission)))

 
print('Относительное значение комиссии')
print('Медиана '+str(statistics.median(OtnKomission)))
print('Размах '+str( max(Komission) - min(OtnKomission)))
print('Среднее значение '+str(statistics.mean(OtnKomission)))
print('Дисперсия '+str(statistics.variance(OtnKomission)))
print('Отклонение '+str(statistics.stdev(OtnKomission)))


