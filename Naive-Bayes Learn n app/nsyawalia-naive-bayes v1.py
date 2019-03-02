# w4llsk1_naive-bayes-first-project boissss
# nama  : M. Naufal Syawali. A
# nim   : 1301164488

test = ("Hello world!")
project = ("This is my first project of Machine Learning")
what = ("Project : Naive-Bayes")

print (test)
print (project)
print (what)

import csv 

#penulisan variabel yang dibutuhkan

dTrain = [] #data train variabel
dTest = [] #data test variabel
finalR = [] #hasil final berupa output
probth50 = 0 #perhitungan jumlah kemungkinan data lebih besar dari 50
probls50 = 0 #perhitungan jumlah kemungkinan data lebih kecil dari 50
dtt = 0 #data train for tasting (objek data dari train yang akan di testing)

#import data train dan data test terlebih dahulu
with open('TestsetTugas1ML.csv') as testFile:
	reader = csv.reader(testFile)
	for i in reader:
		dTest.append(i)
testFile.close()

with open('TrainsetTugas1ML.csv') as trainFile:
	reader = csv.reader(trainFile)
	for i in reader:
		dTrain.append(i)
	dtt = len(dTrain)-1
trainFile.close()

#pembuatan tabel model untuk menentukan atau cek jumlah lebih besar dari 50 atau kurang dari 50

#perhitungan jumlah kemungkinan lebih dari atau kurang dari 50
for j in dTrain:
	if j[8] == ">50K":
		probth50 += 1
	elif j[8] == "<=50K":
		probls50 += 1

jumLbh50 = probth50/dtt
jumKrg50 = probls50/dtt

#Testing 

#Testing untuk data > 50K
def t_probth50(col, valueColumn):
	sum = 0
	for c in dTrain:
		if c[col] == valueColumn and c[8] == ">50K":
			sum += 1
	return sum

#Testing untuk data <=50K
def t_probls50(col, valueColumn):
	sum = 0
	for c in dTrain:
		if c[col] == valueColumn and c[8] == "<=50K":
			sum += 1
	return sum

# function mengembalikan nilai lebih besar dan yang lebih kecil
def morethan(age, workc, edu, ms, occ, rsp, hpw): #data yang ada pada tabel yaitu age, workclass, edu, marital, occupation, relationship, hoursperw)\
	return t_probth50(1, age)/probth50 * t_probth50(2, workc)/probth50 * t_probth50(3, edu)/probth50 * t_probth50(4, ms)/probth50 * t_probth50(5, occ)/probth50 * t_probth50(6, rsp)/probth50 * t_probth50(7, hpw)/probth50 * jumLbh50

def lessthan(age, workc, edu, ms, occ, rsp, hpw):
	return t_probls50(1, age)/probls50 * t_probls50(2, workc)/probls50* t_probls50(3, edu)/probls50 * t_probls50(4, ms)/probls50 * t_probls50(5, occ)/probls50 * t_probls50(6, rsp)/probls50 * t_probls50(7, hpw)/probls50 * jumKrg50

for x in range(0, len(dTest)-1):
	lebih = morethan(dTest[x+1][1], dTest[x+1][2], dTest[x+1][3], dTest[x+1][4], dTest[x+1][5], dTest[x+1][6], dTest[x+1][7])
	kurang = lessthan(dTest[x+1][1], dTest[x+1][2], dTest[x+1][3], dTest[x+1][4], dTest[x+1][5], dTest[x+1][6], dTest[x+1][7])

	if lebih > kurang:
		finalR.append(">50K")
		print(">50")
	else:
		finalR.append("<=50K")
		print("<=50")

print(finalR)

with open('Final_Result_naiveBayes.csv', mode="w", newline="") as tugas1:
	hasilTugas1 = csv.writer(tugas1)
	for t in range(0, len(finalR)):
		hasilTugas1.writerow([finalR[t]])
