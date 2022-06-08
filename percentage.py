import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.chdir('/Users/Yimo/Desktop/assemble/') 
df = pd.read_csv("Percentage.csv")
y = df["Treatment"]
x1 = df["Explorative AML cells"]
x2 = df["Non-explorative AML cells"]

f, ax = plt.subplots(figsize = (12,6))
p = sns.barplot(x = x1, y = y, data = df,color = "lightsteelblue")
#p2 = sns.barplot(x = x2, y = y, data = df, palette=sns.color_palette("ch:s=.25,rot=-.25",1))
p.set(xlim=(0, 80))
p.set(xlabel='Explorative AML cells %')
p.xaxis.set_ticks_position('top')
p.xaxis.set_label_position('top')
for index, value in enumerate(df["Explorative AML cells"]):
       plt.text(value, index, str("{}%".format(value)),va='center', ha = 'left', fontsize = 10)
sns.despine(bottom = True, top = False)
plt.savefig("per.png")







'''

f, ax = plt.subplots(figsize = (12,6))
sns.set_color_codes('pastel')
sns.barplot(x = 'total', y = 'Treatment', data = df,
            label = 'Total AML cells', color = 'blue', edgecolor = 'w')
#change_width(ax, 100)
sns.set_color_codes('muted')
sns.barplot(x = 'Explorative AML cells', y = 'Treatment', data = df,
            label = 'Explorative AML cells', color = 'blue', edgecolor = 'w')
ax.legend(ncol = 2, bbox_to_anchor=(0.5, 1.05), loc = 'center')
sns.despine(left = True, bottom = True)
for index, value in enumerate(df["Explorative AML cells"]):
       plt.text(value, index, str("{}%".format(round(value*100,1))),verticalalignment='center', fontsize = 12)
plt.show()

'''