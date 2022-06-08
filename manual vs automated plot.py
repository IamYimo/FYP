import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as Manualt
import numpy as np
from statannotations.Annotator import Annotator
from scipy.stats import shapiro, levene


os.chdir('/Users/Yimo/Desktop/CL tool/')
velo_001= pd.read_csv("Homing CL.csv")
velo_10 = pd.read_csv("Early CL.csv")
velo_50 = pd.read_csv("Intermediate CL.csv")

velo_001 = velo_001[["Velocity","Tool"]]
velo_10 = velo_10[["Velocity","Tool"]]
velo_50 = velo_50[["Velocity","Tool"]]
velo_001["Experiment"] = "Minimal"
velo_10["Experiment"] = "Early"
velo_50["Experiment"] = "Intermediate"

velo_frame = [velo_001, velo_10, velo_50]
velo = pd.concat(velo_frame)

args = dict(x="Tool", y="Velocity", data=velo, hue="Experiment", hue_order=["Minimal","Early", "Intermediate"], order=['Manual', 'Automated'])
pairs = [
    (("Manual", "Minimal"), ("Automated", "Minimal")),
    (("Manual", "Early"), ("Automated", "Early")),
    (("Manual", "Intermediate"), ("Automated", "Intermediate"))
]

stat1, p1 = shapiro(velo_001["Velocity"])
stat2, p2 = shapiro(velo_10["Velocity"])
stat3, p3 = shapiro(velo_50["Velocity"])
stat4, p4 = levene(velo_001["Velocity"], velo_10["Velocity"])
stat5, p5 = levene(velo_001["Velocity"], velo_50["Velocity"])
stat6, p6 = levene(velo_10["Velocity"], velo_50["Velocity"])
# interpret
alpha = 0.05
if p1 > alpha:
	print('Minimal normal distributed (fail to reject H0)')
else:
	print('Minimal not normal distributed (reject H0)')
if p2 > alpha:
	print('Early normal distributed (fail to reject H0)')
else:
	print('Early not normal distributed (reject H0)')
if p3 > alpha:
	print('Intermediate normal distributed (fail to reject H0)')
else:
	print('Intermediate not normal distributed (reject H0)')
if p4 > alpha:
	print('Minimal vs Early Equal variance')
else:
	print('Minimal vs Early Unequal variance')
if p5 > alpha:
	print('Minimal vs Intermediate Equal variance')
else:
	print('Minimal vs Intermediate Unequal variance')
if p6 > alpha:
	print('Early vs Intermediate Equal variance')
else:
	print('Early vs Intermediate Unequal variance')

sns.set_theme(style="white")
p = sns.catplot(x='Tool', y='Velocity', hue='Experiment', ci = 95, data=velo, capsize = .1, errwidth=1.5, kind='bar', palette=sns.color_palette('flare'))
p.map(sns.stripplot, args["x"], args["y"], args["hue"], hue_order=args["hue_order"], order=args["order"], palette=sns.color_palette('flare'), dodge=True, alpha=0.2, ec='k', linewidth=1)
p.set(xlabel = "Tool Type", ylabel = "Velocity (μm/min)")
for ax_n in p.axes:
    for ax in ax_n:
        annot = Annotator(ax, pairs, **args)
        annot.configure(test='Mann-Whitney', text_format='star', loc='inside', verbose=2)
        annot.apply_test().annotate()

Manualt.savefig('out.png', dpi=300, bbox_inches='tight')
