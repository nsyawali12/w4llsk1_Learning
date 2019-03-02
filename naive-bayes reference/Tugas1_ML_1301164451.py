import csv

datatrain = []
datatest = []
dataoutput = []
lebihdari50 = 0
kurangdari50 = 0
objekdatatrain = 0

with open('TrainsetTugas1ML.csv') as csvFile:
    reader = csv.reader(csvFile)
    for x in reader:
        datatrain.append(x)
    objekdatatrain = len(datatrain)-1

csvFile.close()

with open('TestsetTugas1ML.csv') as csvFile:
    reader = csv.reader(csvFile)
    for x in reader:
        datatest.append(x)

csvFile.close()

#cek jumlah lebih besar 50 atau sebaliknya
for x in datatrain:
    if x[8] == ">50K":
        lebihdari50 = lebihdari50+1

    elif x[8] == "<=50K":
        kurangdari50 = kurangdari50+1

lebih50 = lebihdari50/objekdatatrain
print(lebih50)
kurang50 = kurangdari50/objekdatatrain
print(kurang50)

#probabilitas >50K
def p_lebih(col, valueColumn):
    sum = 0
    for x in datatrain:
        if x[col] == valueColumn and x[8] == ">50K":
            sum = sum + 1
    return sum

#probabilitas <=50K
def p_kurang(col, valueColumn):
    sum = 0
    for x in datatrain:
        if x[col] == valueColumn and x[8] == "<=50K":
            sum = sum + 1
    return sum

def lebihbesar(age, wc, ed, ms, oc, rs, hpw):
    return p_lebih(1, age)/lebihdari50 * p_lebih(2, wc)/lebihdari50 * p_lebih(3, ed)/lebihdari50 * p_lebih(4, ms)/lebihdari50 * p_lebih(5, oc)/lebihdari50 * p_lebih(6, rs)/lebihdari50 * p_lebih(7, hpw)/lebihdari50 * lebih50

def kurangdari(age, wc, ed, ms, oc, rs, hpw):
    return p_kurang(1, age)/kurangdari50 * p_kurang(2, wc)/kurangdari50 * p_kurang(3, ed)/kurangdari50 * p_kurang(4, ms)/kurangdari50 * p_kurang(5, oc)/kurangdari50 * p_kurang(6, rs)/kurangdari50 * p_kurang(7, hpw)/kurangdari50 *kurang50

for x in range(0, len(datatest)-1):
    cekbesar = lebihbesar(datatest[x+1][1], datatest[x+1][2], datatest[x+1][3], datatest[x+1][4], datatest[x+1][5], datatest[x+1][6], datatest[x+1][7])
    cekkecil = kurangdari(datatest[x+1][1], datatest[x+1][2], datatest[x+1][3], datatest[x+1][4], datatest[x+1][5], datatest[x+1][6], datatest[x+1][7])
    print(cekbesar,cekkecil)
    if cekbesar > cekkecil:
        dataoutput.append(">50K")
        print(">50K")
    else:
        dataoutput.append("<=50K")
        print("<=50K")
print(dataoutput)

with open('TebakanTugas3.csv',mode="w",newline="") as task:
    writeTask = csv.writer(task)
    for m in range(0,len(dataoutput)):
        writeTask.writerow([dataoutput[m]])