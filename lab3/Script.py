import pandas as pd
import requests
import numpy as np
import lxml
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import datasets, linear_model

def get_data(url):
    page=pd.read_html(url,encoding='CP1251')
    header=page[6].drop(12).T
    header=header.iloc[1]
    header[0]='Номер УИК'
    data=page[7].drop(12).T
    data.columns=header
    data.reset_index()
    return data

def to_numeric(data):
    data.iloc[:,0]=[int(i.split()[1][1:]) for i in data.iloc[:,0]]
    for i in range(1,12):
        data.iloc[:,i]=pd.to_numeric(data.iloc[:,i])
    for i in range(12,15):
        l=[]
        perc=[]
        for a in data.iloc[:,i]:
            a=a.split()
            l.append(int(a[0]))
            perc.append(float(a[1][:-2]))
        data.iloc[:,i]=l
        data['процент за '+str(data.columns.values[i])]=perc
    return data

url23='http://www.st-petersburg.vybory.izbirkom.ru/region/region/st-petersburg?action=show&tvd=27820001217417&vrn=27820001217413&region=78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217422&type=222'
data=get_data(url23)
data=to_numeric(data)
data.to_csv('data.csv')

def plot(x,y,label,j):

    plt.subplot(1,3,j)
    x=np.array(x).reshape(-1,1)
    y=np.array(y).reshape(-1,1)
    xmin=min(data.iloc[:,1])
    xmax=max(data.iloc[:,1])
    plt.scatter(x,y,linewidth=1)
    plt.title('Голоса за '+label)





plot(data.iloc[:, 1], data.iloc[:, 12], 'Амосова',1)
plot(data.iloc[:, 1], data.iloc[:, 13], 'Беглова',2)
plot(data.iloc[:, 1], data.iloc[:, 14], 'Тихонова',3)

plt.show()