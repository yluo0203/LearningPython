#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 16:30:35 2018

@author: tse-jen.lu
"""

import matplotlib.pyplot as mpt

month1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
Sales1 = [0.5, 0.3, 0.6 ,0.3, 0.9, 0.2, 0.5, 0.7, 0.3, 1.0, 1.1, 0.6 ]
Sales2 = []
for i in range(0,12):
    Sales2.append(Sales1[i])

mpt.plot(month1, Sales2, lw = 2, label = "sales1")
mpt.xlabel("Month")
mpt.ylabel("Dollars")
mpt.legend()
mpt.title("Test for Matplotlib by Python")
mpt.show()