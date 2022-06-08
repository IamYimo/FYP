import pandas as pd
import os
import numpy as np

os.chdir('/Users/Yimo/Desktop/')
data= pd.read_csv("PL.csv")
a = 1
b = data.iloc[1,0]

for i in range(1, len(data)):
    if data.iloc[i,0] != a and data.iloc[i,0] != b:
        a += 1
        b = data.iloc[i,0]
        data.iloc[i,0] = a
    elif data.iloc[i,0] != a and data.iloc[i,0] == b:
        data.iloc[i,0] = a
data.to_csv('PL_new.csv')