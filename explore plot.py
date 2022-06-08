import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statannotations.Annotator import Annotator
from scipy.stats import shapiro, levene


os.chdir('/Users/Yimo/Desktop/assemble')
d_001= pd.read_csv("Homing assemble.csv")
#d_10 = pd.read_csv("Early CL/processed M1-4/parameter/M assemble/Early CL assemble.csv")
#d_50 = pd.read_csv("Intermediate/processed M1-4/parameter/M assemble/Intermediate assemble.csv")

d_001.replace({'Migration':{'Y':'Explorative','N':'Non-explorative'}}, inplace=True)
#d_10.replace({'Migration':{'Y':'Explorative','N':'Non-explorative'}}, inplace=True)
#d_50.replace({'Migration':{'Y':'Explorative','N':'Non-explorative'}}, inplace=True)

args = dict(x="Type", y="Euclidean distance", data=d_001, hue="Migration", hue_order=["Non-explorative", "Explorative"], order=['PL', 'CL'])
pairs = [
    (("PL", "Explorative"), ("PL", "Non-explorative")),
    (("PL", "Explorative"), ("CL", "Explorative")),
    (("PL", "Non-explorative"), ("CL", "Non-explorative")),
    (("CL", "Explorative"), ("CL", "Non-explorative"))
]


Explore = d_001[d_001["Migration"] == "Explorative"]
Non_exp = d_001[d_001["Migration"] == "Non-explorative"]
stat, p = shapiro(Explore["Euclidean distance"])
stat2, p2 = levene(Explore["Euclidean distance"], Non_exp["Euclidean distance"])
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.01
if p > alpha:
	print('normal distributed (fail to reject H0)')
else:
	print('Not normal distributed (reject H0)')
if p2 > alpha:
	print('Equal variance')
else:
	print('Unequal variance')


sns.set_theme(style="white")
p = sns.catplot(x='Type', y='Euclidean distance', hue='Migration', ci = 95, data=d_001, capsize = .1, errwidth=1.5, kind='bar',  palette=sns.color_palette("ch:s=.25,rot=-.25"))
p.map(sns.stripplot, args["x"], args["y"], args["hue"], hue_order=args["hue_order"], order=args["order"], palette=sns.color_palette("ch:s=.25,rot=-.25"), dodge=True, alpha=0.3, ec='k', linewidth=1)
p.set(xlabel = "Treatment", ylabel = "Euclidean Distance (μm)")


for ax_n in p.axes:
    for ax in ax_n:
        annot = Annotator(ax, pairs, **args)
        annot.configure(test='t-test_welch', text_format='star', loc='inside', verbose=2)
        annot.apply_test().annotate()

plt.savefig('out.png', dpi=300, bbox_inches='tight')




'''ax = sns.barplot(x="Type", y="Euclidean distance", data=data, estimator=np.mean, ci = 95, capsize=.1, errcolor = "black")
ax = sns.stripplot(x="Type", y="Euclidean distance", data=data, color="grey", alpha = .3)
ax.set(xlabel='Treatment', ylabel='Euclidean distance (μm/min)', ylim = (0, 0.1))
'''

