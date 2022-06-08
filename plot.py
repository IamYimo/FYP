import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statannot import add_stat_annotation


os.chdir('/Users/Yimo/Desktop/Table data/Intermediate/processed M1-4/parameter/')
#data= pd.read_csv("Directionality/Directionality assembly/Directionality assembly.csv")
data= pd.read_csv("M assemble/Intermediate assemble.csv")

sns.set_theme(style="white")
plt.figure(figsize=(5, 8)) 
ax = sns.barplot(x="Type", y="Directionality", data=data, estimator=np.mean, ci = 95, capsize=.1, errcolor = "black")
ax = sns.stripplot(x="Type", y="Directionality", data=data, palette=sns.color_palette(), dodge=True, alpha=0.3, ec='k', linewidth=1)
ax.set(xlabel='Treatment', ylabel='Directionality', ylim = (0, 0.1))
add_stat_annotation(ax, data=data, x="Type", y="Directionality",
                    box_pairs=[("PL", "CL")],
                    test='Mann-Whitney', text_format='star', loc='inside', verbose=2)

plt.show()