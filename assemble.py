import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from copy import deepcopy

#os.chdir("/Users/Yimo/Desktop/Table data/Homing assay/Processed M1-4/parameter/")
os.chdir("/Users/Yimo/Desktop/")
dis = pd.read_csv("dis 4.csv")
velo = pd.read_csv("velo 4.csv")

namels = []
for i in range(0, len(dis)):
    a = dis.iloc[i, 0]
    namels.append(a)

velocopy = deepcopy(velo)
for i in range(1, len(velo)):
    if velo.iloc[i, 0] not in namels:
        velocopy = velocopy.drop(velo.index[i])


# remember to add column PL and CL

velocopy.to_csv("velo_new 4.csv")





