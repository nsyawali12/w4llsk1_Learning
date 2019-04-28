import random,math
import pandas as pd
data = pd.read_csv("DataTugas3ML2019.txt", delimiter='\t', header=None)
inf = -(math.inf)

def TableRandQ():
    R=[]
    Q=[]
    for i in range(len(data)):
        for j in range(len(data)):
            nodes=[]
            Qnodes=[]
            #input Table Q
            for k in range(4):
                Qnodes.append(-10)
            #input Table R
            if i == 0 :
                if j == 0:
                    nodes.append(inf)
                    nodes.append(data[j+1][i])
                    nodes.append(data[j][i+1])
                    nodes.append(inf)
                elif j == 14:
                    nodes.append(inf)
                    nodes.append(inf)
                    nodes.append(data[j][i+1])
                    nodes.append(data[j-1][i])
                else:
                    nodes.append(inf)
                    nodes.append(data[j+1][i])
                    nodes.append(data[j][i+1])
                    nodes.append(data[j-1][i])
            elif i == 14 :
                if j == 0 :
                    nodes.append(data[j][i-1])
                    nodes.append(data[j+1][i])
                    nodes.append(inf)
                    nodes.append(inf)
                elif j == 14:
                    nodes.append(data[j][i-1])
                    nodes.append(inf)
                    nodes.append(inf)
                    nodes.append(data[j-1][i])
                else:
                    nodes.append(data[j][i-1])
                    nodes.append(data[j+1][i])
                    nodes.append(inf)
                    nodes.append(data[j-1][i])
            else:
                if j == 0:
                    nodes.append(data[j][i-1])
                    nodes.append(data[j+1][i])
                    nodes.append(data[j][i+1])
                    nodes.append(inf)
                elif j == 14:
                    nodes.append(data[j][i-1])
                    nodes.append(inf)
                    nodes.append(data[j][i+1])
                    nodes.append(data[j-1][i])
                else:
                    nodes.append(data[j][i-1])
                    nodes.append(data[j+1][i])
                    nodes.append(data[j][i+1])
                    nodes.append(data[j-1][i])
            R.append(nodes)
            Q.append(Qnodes)
    return R,Q

TR,TQ=TableRandQ()
for i in range(400):
    state=random.randint(0,224)
    while state != 14:
        nextstate=[]
        for j in range(4):
            if TR[state][j] != (-(math.inf)):
                nextstate.append(j)
        arah=random.choice(nextstate)
        if arah == 0:
            Nstate= state -15
        elif arah == 1:
            Nstate = state+1
        elif arah == 2:
            Nstate = state +15
        else:
            Nstate = state-1
        TQ[state][arah] = TR[state][arah]+0.8*max(TQ[Nstate])
        state= Nstate
k=210
score = -2
while k != 14:
    nxt= TQ[k].index(max(TQ[k]))
    score = score + TR[k][nxt]
    if nxt == 0 :
        k = k-15
    elif nxt == 1:
        k=k+1
    elif nxt == 2:
        k=k+15
    else:
        k=k-1

print(pd.DataFrame(TQ))
print('Score Total', score)

