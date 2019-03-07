#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 13:12:14 2019

@author: kerimason
"""

# import os
import csv

election_data = '/Users/kerimason/Desktop/pythonchallenge/PyPoll/election_data.csv'
# print(election_data)

with open(election_data, 'r') as csvfile:
    reader = csv.reader(csvfile)
# print(reader)

    csv_data = []
    
    for row in reader:
        csv_data.append(row)
    #print(row)

#election_data.close()
#
#print(csv_data)