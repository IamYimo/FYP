import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import os

os.chdir("/Users/Yimo/Desktop/Table data/Intermediate/processed M1-4/parameter/M assemble")

def plot_2d(projected, y_train, text, title):
    fig = plt.figure(figsize=(48, 36), dpi=80)
    ax = fig.add_subplot(111)

    p = ax.scatter(projected[:, 0], projected[:, 1], c=y_train)
    ax.set_xlabel('component 1')
    ax.set_ylabel('component 2')
    ax.set_title(title)
    fig.colorbar(p)
    for i,txt in enumerate(text):
        ax.annotate(txt,(projected[:,0][i],projected[:,1][i]))

path = "Intermediate assemble.csv"
X = pd.read_csv(path, usecols=[3, 4, 5])
y = pd.read_csv(path, usecols=[0])

y.replace({'Type':{'PL':0,'CL':1}}, inplace=True)
text = pd.read_csv(path, usecols=[2])
text = np.array(text)

pca = PCA(n_components=2)
projected = pca.fit_transform(X)
y= np.array(y)

plot_2d(projected, y, text, 'Principal Components')
plt.savefig("PCA Intermediate.png")

'''
def plot_2d(projected, y_train, text, title):
    fig = plt.figure(figsize=(12, 9), dpi=80)
    ax = fig.add_subplot(111)

    p = ax.scatter(projected[:, 0], projected[:, 1], c=y_train)
    ax.set_xlabel('component 1')
    ax.set_ylabel('component 2')
    ax.set_title(title)
    fig.colorbar(p)
    for i,txt in enumerate(text):
        ax.annotate(txt,(projected[:,0][i],projected[:,1][i]))'''