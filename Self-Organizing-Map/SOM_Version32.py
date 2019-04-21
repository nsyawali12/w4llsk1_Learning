import math
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from sklearn.preprocessing import MinMaxScaler

Data = np.genfromtxt('Tugas 2 ML Genap 2018-2019 Dataset Tanpa Label.csv', dtype=None, delimiter=',')
sc = MinMaxScaler(feature_range=(0,1))
Data = sc.fit_transform(Data)
Neuron = []
learning_rate = 0.1
tn = 2
sigma = 2
t_sigma = 2

for i in range(20):
    Neuron.append([random.uniform(0,1),random.uniform(0,1)])


def findBMU(x1,x2):
    density = []
    for item in Neuron:
        density.append(math.sqrt((x1-item[0])**2+(x2-item[1])**2))
    min = density[0]
    print('density= ', density)
    j=0
    indeks=j
    for i in density:
        if min > density[j]:
            min=density[j]
            indeks=j
        j = j + 1
    return indeks

def Topological_Neighborhood(w,o):
    S=[]
    T=[]
    i=0
    for item in Neuron:
        S.append(math.sqrt((item[0]-Neuron[w][0])**2+(item[1]-Neuron[w][1])**2))
        T.append(math.exp((-(S[i]**2))/2*(o**2)))
        i=i+1
    return T

def adjust_weight(x1,x2,t,n):
    Y = []
    deltaW=[]
    i=0
    for item in Neuron:
        Y.append([(x1-item[0]), (x2-item[1])])
        deltaW.append([n*Y[i][0]*t[i],n*Y[i][1]*t[i]])
        i=i+1
    return deltaW

def update_ln_sigma(l,tn,o,to,i):
    ln = l*math.exp((i)/tn)
    sgm = o*math.exp((i)/to)
    return  ln,sgm

print(Neuron)
for p in Neuron:
    plt.plot(p[0], p[1], 'ro')

plt.show()

for m in Data:
    plt.plot(m[0], m[1],'bo')
plt.show()
x1=[]
y1=[]
itr= 0
v=0
for j in range(2):
    hasil = []
    learning_rate, sigma = update_ln_sigma(learning_rate, tn, sigma, t_sigma, itr)
    for item in Data:
        x1.append(item[0])
        y1.append(item[1])
        bmu = findBMU(item[0],item[1])
        Tij= Topological_Neighborhood(bmu,sigma)
        Delta = adjust_weight(item[0],item[1],Tij,learning_rate)
        #Update Weight
        iterasi=0
        for k in Neuron:
            k[0]= k[0]+ Delta[iterasi][0]
            k[1] = k[1] + Delta[iterasi][1]
            iterasi=iterasi+1
        hasil.append(bmu)
        print('i=',v,bmu,' ',Neuron)
        v=v+1
        if v==10 :
            break
    itr= itr-1
x=[]
y=[]
for l in Neuron:
    x.append(l[0])
    y.append(l[1])
plt.plot(x1,y1,'bo')
plt.plot(x,y,'ro')


# np.savetxt('TebakanTugas3.csv',hasil,fmt='%i')


plt.show()