import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import os

os.chdir("/Users/Yimo/Desktop/assemble/")

path = "Intermediate assemble.csv"
X = pd.read_csv(path, usecols=[2,3,4,5])
y = pd.read_csv(path, usecols=[0])
pca = PCA(n_components=2)
projected = pca.fit_transform(X)
y.replace({'Type':{'PL':0,'CL':1}}, inplace=True)
y= np.array(y)
plt.figure(figsize=(12, 9), dpi=80)
scatter = plt.scatter(projected[:, 0], projected[:, 1], c=y, cmap='PiYG')
a,b = scatter.legend_elements()
b = ['PL','CL']
mig = pd.read_csv("Intermediate assemble.csv", usecols=[6])
Y = mig[(mig['Migration']=='Y')].index.tolist()
p = projected[Y]
circle, = plt.plot(p[:,0], p[:,1], 'o', ms=15, mec='red', mfc='none', mew=1)
a = a + [circle]
b = b + ['Explorative cell']
legend1 = plt.legend(a, b, prop={'size': 20})

font2 = {'weight' : 'normal', 'size' : 20}
plt.xlabel('PC 1', font2)
plt.ylabel('PC 2', font2)
plt.title('Principal Components',font2)

plt.savefig("PCA Intermediate.png")






'''
def plot_2d(projected, y_train, text, title):
    fig = plt.figure(figsize=(48, 36), dpi=80)
    ax = fig.add_subplot(111)

    p = ax.scatter(projected[:, 0], projected[:, 1], c=y_train)
    ax.set_xlabel('component 1')
    ax.set_ylabel('component 2')
    ax.set_title(title)
    fig.colorbar(p)
    for i,txt in enumerate(text):
        if text == "Y":
            ax.plot(txt,(projected[:,0][i],projected[:,1][i]))

path = "Intermediate CL assemble.csv"
X = pd.read_csv(path, usecols=[2,3,4])
y = pd.read_csv(path, usecols=[5])

y.replace({'Type':{'PL':0,'CL':1}}, inplace=True)
text = pd.read_csv("Intermediate CL assemble.csv", usecols=[6])
text = np.array(text)

pca = PCA(n_components=2)
projected = pca.fit_transform(X)
y= np.array(y)

plot_2d(projected, y, text, 'Principal Components')
plt.savefig("PCA Intermediate")


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