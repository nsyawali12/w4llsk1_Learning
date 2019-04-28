import gym 
import itertools 
import matplotlib 
import matplotlib.style 
import numpy as np 
import pandas as pd 
import sys
import random
import math

#import file data tugas 3
dfile3 = pd.read_csv("DataTugas3ML2019.txt", delimiter='\t', header=None)
inf = -(math.inf) #di set infinite

#Q learning buat table si data tugas
def TRandomQ():
  Q = []
  Reward = []
  for i in range(len(dfile3)):
    for j in range(len(dfile3)):
      node = []
      Qnode = []
      #Masukkan table Q untuk QLearn
      for k in range(4):
        Qnode.append(-10)
      #Input Table R untuk Table Reward
      if i == 0 :

        if j == 0:
          node.append(inf)
          node.append(dfile3[j+1][i])
          node.append(dfile3[j][i+1])
          node.append(inf)

        elif j == 14:
          node.append(inf)
          node.append(inf)
          node.append(dfile3[j][i+1])
          node.append(dfile3[j-1][i])

        else:
          node.append(inf)
          node.append(dfile3[j+1][i])
          node.append(dfile3[j][i+1])
          node.append(dfile3[j-1][i])
      
      elif i == 14 :

        if j == 0 :
          node.append(dfile3[j][i-1])
          node.append(dfile3[j+1][i])
          node.append(inf)
          node.append(inf)

        elif j == 14:
          node.append(dfile3[j][i-1])
          node.append(inf)
          node.append(inf)
          node.append(dfile3[j-1][i])

        else:
          node.append(dfile3[j][i-1])
          node.append(dfile3[j+1][i])
          node.append(inf)
          node.append(dfile3[j-1][i])
      
      else:
        
        if j == 0:
          node.append(dfile3[j][i-1])
          node.append(dfile3[j+1][i])
          node.append(dfile3[j][i+1])
          node.append(inf)
        
        elif j == 14:

          node.append(dfile3[j][i-1])
          node.append(inf)
          node.append(dfile3[j][i+1])
          node.append(dfile3[j-1][i])

        else :
          node.append(dfile3[j][i-1])
          node.append(dfile3[j+1][i])
          node.append(dfile3[j][i+1])
          node.append(dfile3[j-1][i])
      Reward.append(node)
      Q.append(Qnode)
  
  return Reward, Q

tReward, tQ = TRandomQ()
for i in range (600):
  state = random.randint(0, 224)
  while state != 14 :
    nextState  = []
    for j in range(4):
      if tReward[state][j] != (-(math.inf)):
        nextState.append(j)
    
    arahs = random.choice(nextState)
    if arahs == 0:
      nextState = state-15
    elif arahs ==1 :
      nextState = state+1
    elif arahs == 2 :
      nextState = state+15
    else:
      nextState = state-1
    tQ[state][arahs] = tReward[state][arahs]+0.8*max(tQ[nextState])
    state = nextState

k = 210
skor = -4
while k != 14:
  next = tQ[k].index(max(tQ[k]))
  skor = skor + tReward[k][next]
  
  if next == 0:
    k = k-15
  elif next == 1:
    k = k + 1
  elif next == 2:
    k = k + 15
  else:
    k = k- 1
  

print(pd.DataFrame(tQ))
print('Jumlah Skor total', skor)