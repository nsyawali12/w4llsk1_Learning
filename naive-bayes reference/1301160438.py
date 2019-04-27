# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 22:57:31 2019

@author: madit
"""
import pandas as pd
from collections import Counter

#inisiasi variabel
head= ['age','workclass','education','marital-status','occupation','relationship','hours-per-week']
countup = []
countdown = []
hasil=[]
#loading data csv ke variabel
dftrain = pd.read_csv('TrainsetTugas1ML.csv')   
dftest = pd.read_csv('TestsetTugas1ML.csv')
#penentuan kondisi label yang akan dipakai
dfup = dftrain[dftrain['income']== '>50K']
dfdown = dftrain[dftrain['income']== '<=50K']
#perhitungan tiap fitur sesuai dengan kondisi label yang ditentukan
for x in head:
    countup.append(pd.Series(dfup[x].str.replace('[\[\]\']','').str.split(',').map(Counter).sum()))
    countdown.append(pd.Series(dfdown[x].str.replace('[\[\]\']','').str.split(',').map(Counter).sum()))
#perhitungan dengan teorema naive bayes
for index, row in dftest.iterrows():
   up=(countup[0][row['age']]/countup[0].sum())*(countup[1][row['workclass']]/countup[1].sum())*(countup[2][row['education']]/countup[2].sum())*(countup[3][row['marital-status']]/countup[3].sum())*(countup[4][row['occupation']]/countup[4].sum())*(countup[5][row['relationship']]/countup[5].sum())*(countup[6][row['hours-per-week']]/countup[6].sum())*(dfup.index.size/dftrain.index.size)
   down=(countdown[0][row['age']]/countdown[0].sum())*(countdown[1][row['workclass']]/countdown[1].sum())*(countdown[2][row['education']]/countdown[2].sum())*(countdown[3][row['marital-status']]/countdown[3].sum())*(countdown[4][row['occupation']]/countdown[4].sum())*(countdown[5][row['relationship']]/countdown[5].sum())*(countdown[6][row['hours-per-week']]/countdown[6].sum())*(dfdown.index.size/dftrain.index.size)
#membandingkan hasil dengan kondisi label >50k atau <=50k
hasil.append('>50K') if up>down else hasil.append('<=50K')
       
#data disimpan ke csv
pd.DataFrame(hasil).to_csv("TebakanTugas1ML.csv",index=False, header=False)