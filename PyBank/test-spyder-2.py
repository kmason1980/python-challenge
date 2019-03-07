#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 13:38:11 2019

@author: kerimason
"""

# import os
# import csv

election_data = open('/Users/kerimason/Desktop/pythonchallenge/PyPoll/election_data.csv', 'r')

#reader = csv.reader(election_data)
reader = election_data.read()

election_data.close()

csv_data = []

for row in reader:
    csv_data.append(row)
    

print(csv_data)
