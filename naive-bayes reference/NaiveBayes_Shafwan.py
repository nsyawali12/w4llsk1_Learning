import csv

with open('TrainsetTugas1ML.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    TrainSet = []
    age = []
    workclass = []
    edu = []
    status = []
    occupation = []
    relationship = []
    hpw = []
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            age.append([row[1],row[8]])
            workclass.append([row[2],row[8]])
            edu.append([row[3],row[8]])
            status.append([row[4],row[8]])
            occupation.append([row[5], row[8]])
            relationship.append([row[6], row[8]])
            hpw.append([row[7], row[8]])

with open('TestsetTugas1ML.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    TestSet = []
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            TestSet.append([str(row[1]),str(row[2]),str(row[3]), str(row[4]), str(row[5]),str(row[6]), str(row[7])])

Py50ats = 0
Py50bwh = 0
pa50ats = 0
pa50bwh = 0
po50ats = 0
po50bwh = 0
for idx in range(0,len(age)):
    if age[idx][0] == 'young' and age[idx][1] == '>50K':
        Py50ats = Py50ats + 1
    elif age[idx][0] == 'young' and age[idx][1] == '<=50K':
        Py50bwh = Py50bwh + 1

    if age[idx][0] == 'adult' and age[idx][1] == '>50K':
        pa50ats = pa50ats + 1
    elif age[idx][0] == 'adult' and age[idx][1] == '<=50K':
        pa50bwh = pa50bwh + 1

    if age[idx][0] == 'old' and age[idx][1] == '>50K':
        po50ats = po50ats + 1
    elif age[idx][0] == 'old' and age[idx][1] == '<=50K':
        po50bwh = po50bwh + 1

P_50ats = 0
P_50bwh = 0
for idx in range(0,len(age)):
    if age[idx][1] == '>50K':
        P_50ats = P_50ats + 1
    elif age[idx][1] == '<=50K':
        P_50bwh = P_50bwh + 1

PYoungAtas = Py50ats / P_50ats
PYoungBawah = Py50bwh / P_50bwh
PAdultAtas = pa50ats / P_50ats
PAdultBawah = pa50bwh / P_50bwh
POldAtas = pa50ats / P_50ats
POldBawah = pa50bwh / P_50bwh

privateLebih = 0
privateKurang = 0
localLebih = 0
localKurang = 0
selfLebih = 0
selfKurang = 0
for idx in range(0,len(workclass)):
    if workclass[idx][0] == 'Private' and workclass[idx][1] == '>50K':
        privateLebih = privateLebih + 1
    elif workclass[idx][0] == 'Private' and workclass[idx][1] == '<=50K':
        privateKurang = privateKurang + 1
    if workclass[idx][0] == 'Local-gov' and workclass[idx][1] == '>50K':
        localLebih = localLebih + 1
    elif workclass[idx][0] == 'Local-gov' and workclass[idx][1] == '<=50K':
        localKurang = localKurang + 1
    if workclass[idx][0] == 'Self-emp-not-inc' and workclass[idx][1] == '>50K':
        selfLebih = selfLebih + 1
    elif workclass[idx][0] == 'Self-emp-not-inc' and workclass[idx][1] == '<=50K':
        selfKurang = selfKurang + 1

PPrivateLebih = privateLebih / P_50ats
PPrivateKurang = privateKurang / P_50bwh
PLocalLebih = localLebih / P_50ats
PLocalKurang = localKurang / P_50bwh
PSelfLebih = selfLebih / P_50ats
PSelfKurang = selfKurang / P_50bwh

collegeLebih = 0
collegeKurang = 0
bachLebih = 0
bachLurang = 0
gradLebih = 0
gradKurang = 0
for idx in range(0,len(edu)):
    if edu[idx][0] == 'Some-college' and edu[idx][1] == '>50K':
        collegeLebih = collegeLebih + 1
    elif edu[idx][0] == 'Some-college' and edu[idx][1] == '<=50K':
        collegeKurang = collegeKurang + 1
    if edu[idx][0] == 'Bachelors' and edu[idx][1] == '>50K':
        bachLebih = bachLebih + 1
    elif edu[idx][0] == 'Bachelors' and edu[idx][1] == '<=50K':
        bachLurang = bachLurang + 1
    if edu[idx][0] == 'HS-grad' and edu[idx][1] == '>50K':
        gradLebih = gradLebih + 1
    elif edu[idx][0] == 'HS-grad' and edu[idx][1] == '<=50K':
        gradKurang = gradKurang + 1

PCollegeLebih = collegeLebih / P_50ats
PCollegeKurang = collegeKurang /P_50bwh
PBachLebih = bachLebih / P_50ats
PBachKurang = bachLurang / P_50bwh
PGradLebih = gradLebih / P_50ats
PGradKurang = gradKurang / P_50bwh

MarriedLebih = 0
MarriedKurang = 0
NeverLebih = 0
NeverKurang = 0
DivorcedLebih = 0
DivorcedKurang = 0
for idx in range(0,len(status)):
    if status[idx][0] == 'Married-civ-spouse' and status[idx][1] == '>50K':
        MarriedLebih = MarriedLebih + 1
    elif status[idx][0] == 'Married-civ-spouse' and status[idx][1] == '<=50K':
        MarriedKurang = MarriedKurang + 1
    if status[idx][0] == 'Never-married' and status[idx][1] == '>50K':
        NeverLebih = NeverLebih + 1
    elif status[idx][0] == 'Never-married' and status[idx][1] == '<=50K':
        NeverKurang = NeverKurang + 1
    if status[idx][0] == 'Divorced' and status[idx][1] == '>50K':
        DivorcedLebih = DivorcedLebih + 1
    elif status[idx][0] == 'Divorced' and status[idx][1] == '<=50K':
        DivorcedKurang = DivorcedKurang + 1

PMarriedLebih = MarriedLebih / P_50ats
PMarriedKurang = MarriedKurang / P_50bwh
PNeverLebih = NeverLebih / P_50ats
PNeverKurang = NeverKurang / P_50bwh
PDivorcedLebih = DivorcedLebih / P_50ats
PDivorcedKurang = DivorcedKurang / P_50bwh

profLebih = 0
profKurang = 0
craftLebih = 0
craftKurang = 0
execLebih = 0
execKurang = 0
for idx in range(0,len(occupation)):
    if occupation[idx][0] == 'Prof-specialty' and occupation[idx][1] == '>50K':
        profLebih = profLebih + 1
    elif occupation[idx][0] == 'Prof-specialty' and occupation[idx][1] == '<=50K':
        profKurang = profKurang + 1
    if occupation[idx][0] == 'Craft-repair' and occupation[idx][1] == '>50K':
        craftLebih = craftLebih + 1
    elif occupation[idx][0] == 'Craft-repair' and occupation[idx][1] == '<=50K':
        craftKurang = craftKurang + 1
    if occupation[idx][0] == 'Exec-managerial' and occupation[idx][1] == '>50K':
        execLebih = execLebih + 1
    elif occupation[idx][0] == 'Exec-managerial' and occupation[idx][1] == '<=50K':
        execKurang = execKurang + 1

PProfLebih = profLebih / P_50ats
PProfKurang = profKurang / P_50bwh
PCraftLebih = craftLebih / P_50ats
PCraftKurang = craftKurang / P_50bwh
PExecLebih = execLebih / P_50ats
PExecKurang = execKurang / P_50bwh

husbandLebih = 0
husbandKurang = 0
notfailyLebih = 0
notfamilyKurang = 0
childLebih = 0
childKurang = 0
for idx in range(0,len(relationship)):
    if relationship[idx][0] == 'Husband' and relationship[idx][1] == '>50K':
        husbandLebih = husbandLebih + 1
    elif relationship[idx][0] == 'Husband' and relationship[idx][1] == '<=50K':
        husbandKurang = husbandKurang + 1
    if relationship[idx][0] == 'Not-in-family' and relationship[idx][1] == '>50K':
        notfailyLebih = notfailyLebih + 1
    elif relationship[idx][0] == 'Not-in_family' and relationship[idx][1] == '<=50K':
        notfamilyKurang = notfamilyKurang + 1
    if relationship[idx][0] == 'Own-child' and relationship[idx][1] == '>50K':
        childLebih = childLebih + 1
    elif relationship[idx][0] == 'Own-child' and relationship[idx][1] == '<=50K':
        childKurang = childKurang + 1

PHusbandLebih = husbandLebih / P_50ats
PHusbandKurang = husbandKurang / P_50bwh
PNotFamilyLebih = notfailyLebih / P_50ats
PNotfamilyKurang = notfamilyKurang / P_50bwh
PChildLebih = childLebih / P_50ats
PChildKurang = childKurang / P_50bwh

normalLebih = 0
normalKurang = 0
lowLebih = 0
lowKurang = 0
manyLebih = 0
manyKurang = 0
for idx in range(0,len(hpw)):
    if hpw[idx][0] == 'normal' and hpw[idx][1] == '>50K':
        normalLebih = normalLebih + 1
    elif hpw[idx][0] == 'normal' and hpw[idx][1] == '<=50K':
        normalKurang = normalKurang + 1
    if hpw[idx][0] == 'low' and hpw[idx][1] == '>50K':
        lowLebih = lowLebih + 1
    elif hpw[idx][0] == 'low' and hpw[idx][1] == '<=50K':
        lowKurang = lowKurang + 1
    if hpw[idx][0] == 'many' and hpw[idx][1] == '>50K':
        manyLebih = manyLebih + 1
    elif hpw[idx][0] == 'many' and hpw[idx][1] == '<=50K':
        manyKurang = manyKurang + 1

PNormalLebih = normalLebih / P_50ats
PNormalKurang = normalKurang / P_50bwh
PLowLebih = lowLebih / P_50ats
PLowKurang = lowKurang / P_50bwh
PManyLebih = manyLebih / P_50ats
PManyKurang = manyKurang / P_50bwh

Yes = []
No = []
income = []
with open('TebakanTugas1.csv', 'w', newline="") as new_file:
    csv_writer = csv.writer(new_file,delimiter=' ')
    for idx in range(0, len(TestSet)):
        if TestSet[idx][0] == 'young':
            Yes = PYoungAtas * 1
            No = PYoungBawah * 1
        elif TestSet[idx][0] == 'adult':
            Yes = PAdultAtas * 1
            No = PAdultBawah * 1
        elif TestSet[idx][0] == 'old':
            Yes = POldAtas * 1
            No = POldBawah * 1
        if TestSet[idx][1] == 'Private':
            Yes = Yes * PPrivateLebih
            No = No * PPrivateKurang
        elif TestSet[idx][1] == 'Local-gov':
            Yes = Yes * PLocalLebih
            No = No * PLocalKurang
        elif TestSet[idx][1] == 'Self-emp-not-inc':
            Yes = Yes * PSelfLebih
            No = No * PSelfKurang
        if TestSet[idx][2] == 'HS-grad':
            Yes = Yes * PGradLebih
            No = No * PGradKurang
        elif TestSet[idx][2] == 'Bachelors':
            Yes = Yes * PBachLebih
            No = No * PBachKurang
        elif TestSet[idx][2] == 'Some-college':
            Yes = Yes * PCollegeLebih
            No = No * PCollegeKurang
        if TestSet[idx][3] == 'Never-married':
            Yes = Yes * PNeverLebih
            No = No * PNeverKurang
        elif TestSet[idx][3] == 'Married':
            Yes = Yes * PMarriedLebih
            No = No * PMarriedKurang
        elif TestSet[idx][3] == 'Divorced':
            Yes = Yes * PDivorcedLebih
            No = No * PDivorcedKurang
        if TestSet[idx][4] == 'Craft-repair':
            Yes = Yes * PCraftLebih
            No = No * PCraftKurang
        elif TestSet[idx][4] == 'Exec-managerial':
            Yes = Yes * PExecLebih
            No = No * PExecKurang
        elif TestSet[idx][4] == 'Prof-specialty':
            Yes = Yes * PProfLebih
            No = No * PProfKurang
        if TestSet[idx][5] == 'Not-in-family':
            Yes = Yes * PNotFamilyLebih
            No = No * PNotfamilyKurang
        elif TestSet[idx][5] == 'Husband':
            Yes = Yes * PHusbandLebih
            No = No * PHusbandKurang
        elif TestSet[idx][5] == 'Own-child':
            Yes = Yes * PChildLebih
            No = No * PChildKurang
        if TestSet[idx][6] == 'normal':
            Yes = Yes * PNormalLebih
            No = No * PNormalKurang
        elif TestSet[idx][6] == 'low':
            Yes = Yes * PLowLebih
            No = No * PLowKurang
        elif TestSet[idx][6] == 'many':
            Yes = Yes * PManyLebih
            No = No * PManyKurang
        if Yes > No:
            income = '>50K'
        else:
            income = '<=50K'
        csv_writer.writerow(income)

print('"TebakanTugas1.csv" sudah tersimpan')