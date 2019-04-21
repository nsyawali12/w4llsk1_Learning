import math
import random
import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt
from matplotlib import patches as patches
import matplotlib.lines as mlines

daset = np.genfromtxt('Tugas2_ML_Genap_2018-2019_DatasetTanpaLabel.csv', dtype = None, delimiter = ',')

#Temporary Suggestion :D
#There 2 class or column of object on csv file, so i set 2 for each tn
#sigma nr nSigma = grade of Sigma
tn = 2

nSigma = 2

tSigma = 2

Nrn = [] #variabel menampung kelas neuron

learn_rate = 0.2

#jumlah iterasi bebas saya set 6, setiap iterasi ngebandingin 600
for i in range(6):
	Nrn.append([random.uniform(0.0,1.0),random.uniform(0.0,1.0)])

#function buat cari BMU, cari nilai BMU yang paling kecil
def searchBMU(x1,x2):
	density = [] #Cari Jarak Weight dengan Data yang lagi di akses
	for itemN in Nrn :
		density.append(math.sqrt((x1-itemN[0])**2+(x2-itemN[1])**2))
	min = density[0]
	j = 0
	nIdx = j
	for i in density:
		if min > i:
			min = i
			nIdx = j
		j = j + 1
	return nIdx
	#the current weight is reduced by BMU Value

#Find Topological Neighborhood
def THood(we, ob):
	S = []
	T = []
	i = 0
	#S & T must exist like Neightborhood function
	for itemN in Nrn:
		S.append(math.sqrt((itemN[0]-Nrn[we][0])**2+(itemN[1]-Nrn[we][1])**2))
		T.append(math.exp((-(S[i]**2))/2*(ob**2)))
		i = i + 1
	return S, T

#This function is for Adjust the Weight
def adjust_weight(x1,x2,t,n):
	Y = []
	deltaW = [] #see the different with deltaW
	i = 0
	for itemN in Nrn:
		Y.append([(x1-itemN[0]), (x2-itemN[1])])
		deltaW.append([n*Y[i][0]*t[i], n*Y[i][1]*t[i]])
		i = i + 1
	return deltaW

#Update learning rate & sigma
def LearnSigmaUpd(l, tn, ob,to):
	lr = l*math.exp((-1)/tn)
	sig = ob*math.exp((-1)/to)
	return lr, sig

#for 2 sigma
for j in range(20): 
	res = [] #This Array is for the result
	for itemN in daset:
		vBmu = searchBMU(itemN[0], itemN[1])
		Sij, Tij = THood(vBmu, nSigma) #Equation need ij each S or T
		Delta = adjust_weight(itemN[0], itemN[1], Tij, learn_rate)
		#Update Weight
		iteration = 0
		for n in Nrn:
			n[0] = n[0] + Delta[iteration][0]
			n[0] = n[1] + Delta[iteration][0]
			iteration = iteration + 1
		res.append(vBmu)
	learn_rate, nSigma = LearnSigmaUpd(learn_rate, tn, nSigma, tSigma)

#Output the result or guest :D
np.savetxt('TebakanTugas2.csv', res, fmt='%i')

#Algorith Explaining
#Step 1 : import the data csv
#Step 2 : Initialize Weight
#Step 3 : Find BMU
#Step 4 : Find Topological Neighborhood of The BMU
#Step 5 : Find Current Weight Reduced by BMU Value or the Update of Weight
