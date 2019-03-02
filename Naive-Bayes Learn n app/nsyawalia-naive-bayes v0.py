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
					arrayTab