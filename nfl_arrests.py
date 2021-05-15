# -*- coding: utf-8 -*-
"""
Created on Sat May 15 13:58:43 2021

@author: Keenan Kunc
"""

#1
#Read csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nfl = pd.read_csv("nfl_arrests_2011-2015.csv")

#2
#Important variables
    #total arrests
    #new column for home team wins--1 for win, 0 for loss

nfl["homewin"] = nfl["home_score"] > nfl["away_score"]

    
#3
#Linear regression for correlation between home wins and total arrests
    #Graph/visualization
all_arrests = np.sum(nfl["arrests"])
mean_arrests_allgames = np.mean(nfl["arrests"])
num_games = np.sum(nfl["homewin"])

grouped_nfl = nfl.groupby("homewin")
group_arrests = grouped_nfl.mean("arrests")
group_arrests = group_arrests["arrests"]

print(group_arrests[0])
print(group_arrests[1])

print(all_arrests)
print(mean_arrests_allgames)
print(num_games)
#print(group_arrests)

arrests_plot = group_arrests.plot.bar()
#print(arrests_plot)
#plt.bar(group_arrests.index, group_arrests)
#print(type(group_arrests))

#plt.bar(nfl["homewin"], nfl["arrests"])

nfl["pointdiff"] = nfl["home_score"] - nfl["away_score"]

print(nfl[["arrests"]].describe())

import seaborn as sb

pointdiff_arrests = sb.lmplot(x = "pointdiff", y = "arrests", data=nfl)
#print(pointdiff_arrests)

grouped_team = nfl.groupby("home_team").mean()["arrests"].dropna().sort_values(ascending = False)

print(grouped_team.describe())
team_arrests = grouped_team.plot.bar()

print(arrests_plot)
print(team_arrests)
