# w4llsk1_naive-bayes-first-project boissss
test = ("Hello world!")
project = ("This is my first project of Machine Learning")
what = ("Project : Naive-Bayes")

print (test)
print (project)
print (what)

# import file using pandas and numpy for read the csv

import pandas as pd
import numpy as np

dframe1 = pd.DataFrame(pd.read_csv('TrainsetTugas1ML.csv').as_matrix().tolist()) 
dtrain = np.asarray(dframe1)

stat = []
for i in range(1,9):
	stat.append(list(set(dframe1[i].tolist())))

# the reason why range 1-9 because the data train got 9 column

# now creating the table model first before testing phase

arrayTab = np.zeros((7,4,2)) #using zeros library 7 shape, 4 data type, 2row major
s_data = np.zeros((2))

for data in dtrain:
	for j in range(1, len(data)-1):
		for k in range(len(stat[j-1])):
			if(data[j] == stat[j-1][k]):
				if(data[8] == stat[7][0]):
					arrayTab[j-1][k][0] += 1
				else :
					arrayTab[j-1][k][1] += 1

		if(data[8] == stat[7][0]):
			arrayTab[j-1][3][0] += 1
		else:
			arrayTab[j-1][3][0] += 1
	if(data[8] == stat[7][0]):
		s_data[0] += 1
	else:
		s_data[1] += 1

# Testing 
dframe1 = pd.DataFrame(pd.read_csv('TestsetTugas1ML.csv').as_matrix().tolist())
dTest = np.asarray(dframe1)
resT = np.ones((len(dTest), 2)) #result testing
index = 0
for data in dTest:
	for j in range(1, len(data)):
		for k in range(len(stat[j-1])):
			if(data[j] == stat[j-1][k]):
				resT[index][0] *= arrayTab[j-1][k][0] / arrayTab[j-1][3][0]
				resT[index][1] *= arrayTab[j-1][k][1] / arrayTab[j-1][3][1]
	resT[index][0] *= s_data[0] / sum(s_data)
	resT[index][1] *= s_data[0] / sum(s_data)
	index += 1

resT = np.argmax(resT, axis = 1)
resFinal = []
for i in range(len(resT)):
	if(resT[i] == 0):
		resFinal.append("<=50K")
	else:
		resFinal.append(">50K")

dframe1[8] = resFinal
dframe1.to_csv("result_final_testing.csv", encoding="utf-8", index=False, header=False)