import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statannotations.Annotator import Annotator
from scipy.stats import shapiro


os.chdir('/Users/Yimo/Desktop/')
data= pd.read_csv("Velocity early ntermediate framed vs unframed.csv")

args = dict(x="Frame", y="Velocity", data=data, hue="Type", hue_order=["PL", "CL"], order=['framed', 'unframed'])
pairs = [
    (("framed", "PL"), ("framed", "CL")),
    (("framed", "PL"), ("unframed", "PL")),
    (("framed", "CL"), ("unframed", "CL")),
    (("unframed", "PL"), ("unframed", "CL"))
]

'''
Explore = d_001[d_001["Behavior"] == "PL"]
Non_exp = d_001[d_001["Behavior"] == "CL"]
stat, p = shapiro(Non_exp["Velocity"])
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('normal distributed (fail to reject H0)')
else:
	print('Not normal distributed (reject H0)')

'''

sns.set_theme(style="white")
p = sns.catplot(x='Frame', y='Velocity', hue='Type', ci = 95, data=data, kind='bar', palette=sns.color_palette("light:#5A9"))
p.map(sns.stripplot, args["x"], args["y"], args["hue"], hue_order=args["hue_order"], order=args["order"], palette=sns.color_palette("light:#5A9"), dodge=True, alpha=0.3, ec='k', linewidth=1)
p.set(xlabel = "Process", ylabel = "Velocity (μm/min)")


for ax_n in p.axes:
    for ax in ax_n:
        annot = Annotator(ax, pairs, **args)
        annot.configure(test='Mann-Whitney', text_format='star', loc='inside', verbose=2)
        annot.apply_test().annotate()

plt.savefig("frame.png")