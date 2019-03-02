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


# the reason why range 1-9 because the data train got 9 column

# now creating the table model first before testing phase

