#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import radarboxplot

x = np.loadtxt("figure2raw.csv", delimiter=";", dtype="int", skiprows=1, usecols=range(1, 9))
#x = x / x.max(axis=0)
y = []

with open("figure2raw.csv") as data:
    colNames = next(data).rstrip().split(";")[1:]
    for line in data:
        y.append(line.split(";")[0])
y = np.array(y)

radarboxplot.radarboxplot(x, y, colNames, plotMedian=True, color=["dimgrey", "grey"])
plt.savefig("fastgenplot.svg")
