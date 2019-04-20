import math
import random
import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt
from matplotlib import patches as patches
import matplotlib.lines as mlines

daset = pd.read_csv("Tugas2_ML_Genap_2018-2019_DatasetTanpaLabel.csv")
Nrn = [] #variabel menampung kelas neuron

learn_rate = 0.2

tn = 3

nSigma = 3

t_sigma = 3

#jumlah iterasi bebas, setiap iterasi ngebandingin 600


