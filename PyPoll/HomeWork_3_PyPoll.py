#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 13:46:15 2019

@author: kerimason
"""

import os
import csv

election_data = open('/Users/kerimason/Desktop/pythonchallenge/PyPoll/election_data.csv', 'r')

reader = csv.reader(election_data)
csv_data = []
for row in reader:
    csv_data.append(row)
election_data.close()
print(csv_data)



