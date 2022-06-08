import pandas as pd
import os
import numpy as np

os.chdir('/Users/Yimo/Desktop/')
data= pd.read_csv("Intermediate automated CL for frame.csv")
n = 0
a = data.iloc[1,0]
datacopy = data.copy(deep = True)
for i in range(1, len(data)):
    if data.iloc[i,0] == a:
        n += 1
        while n >= 28:
            datacopy = datacopy.drop(data.index[i])
            break
    elif data.iloc[i,0] != a:
        n = 0
        a = data.iloc[i,0]

datacopy.to_csv('Intermediate automated CL framed.csv')