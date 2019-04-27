import math
import random
import numpy as np

Data = np.genfromtxt('Tugas 2 ML Genap 2018-2019 Dataset Tanpa Label.csv', dtype=None, delimiter=',')
Neuron = []
learning_rate = 0.1
#hardcode dari mela
tn = 2
sigma = 2
t_sigma = 2

#jumlah iterasi bebas, setiap iterasi ngebandingin 600 data, baru update learning rate dan sigma
for i in range(6):
    Neuron.append([random.uniform(0.0,1.0),random.uniform(0.0,1.0)])

#cari BMU tuh yang paling kecil
def findBMU(x1,x2):
    density = []
    for item in Neuron:
        density.append(math.sqrt((x1-item[0])**2+(x2-item[1])**2))
    min = density[0]
    j=0
    indeks=j
    for i in density:
        if min > i:
            min=i
            indeks=j
        j = j + 1
    return indeks
    #the current weight is reduced by the BMU Value

#Cari topological Neighborhood
def Topological_Neighborhood(w,o): 
    S=[]
    T=[]
    i=0
    for item in Neuron:
        S.append(math.sqrt((item[0]-Neuron[w][0])**2+(item[1]-Neuron[w][1])**2))
        T.append(math.exp((-(S[i]**2))/2*(o**2)))
        i=i+1
    return S,T

#Adjust the weight of
def adjust_weight(x1,x2,t,n):
    Y = []
    deltaW=[]
    i=0
    for item in Neuron:
        Y.append([(x1-item[0]), (x2-item[1])])
        deltaW.append([n*Y[i][0]*t[i],n*Y[i][1]*t[i]])
        i=i+1
    return deltaW

#ngeupdate learning rate dan sigma
def update_ln_sigma(l,tn,o,to):
    ln = l*math.exp((-1)/tn)
    sgm = o*math.exp((-1)/to)
    return  ln,sgm

for j in range(2):
    hasil = []
    for item in Data:
        bmu = findBMU(item[0],item[1])
        Sij,Tij= Topological_Neighborhood(bmu,sigma)
        Delta = adjust_weight(item[0],item[1],Tij,learning_rate)
        #Update Weight
        iterasi=0
        for k in Neuron:
            k[0]= k[0]+ Delta[iterasi][0]
            k[1] = k[1] + Delta[iterasi][1]
            iterasi=iterasi+1
        hasil.append(bmu)
    learning_rate,omega= update_ln_omega(learning_rate,tn,sigma,t_sigma)
np.savetxt('TebakanTugas3.csv',hasil,fmt='%i')

#setiap 2a 2b 2c beres weight harus di update