#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 14:18:45 2019

@author: kerimason
"""

import os
import csv

fileBudget_Data = open('budget_data.csv', 'r')
reader = csv.reader(fileBudget_Data)
csv_data = []
for row in reader:
    csv_data.append(row)
fileBudget_Data.close()
print(csv_data)


