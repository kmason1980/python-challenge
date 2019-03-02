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

#number of months in dataset
dates = []
for r in csv_data[1:]:
    dates.append(r[0])
    
n_months = len(set(dates))

print(n_months)

#sum profit and loss
#can not run any functions until the row is isolated using the following
#line 34 is a nested function 
profit_loss = []
for r in csv_data[1:]:
    profit_loss.append(float(r[1]))
    
net_profit = sum(profit_loss)    
print(net_profit)

#Answer to the average of the changes in "Profit/Losses" over the entire period
average_profit_loss = net_profit / n_months
print(average_profit_loss)

#The average of the changes in "Profit/Losses" over the entire period
data = list(zip(dates, profit_loss))
changes = []
changes_log = []
for idx,d in enumerate(data[:-1]):
    da = d[0]
    da_next = data[idx+1][0]
    pr = d[1]
    pr_next = data[idx+1][1]
    
    change = pr_next-pr
    changes.append(change)
    changes_log.append((da_next,change))
    
avg_change = sum(changes)/len(changes)
    
print(avg_change)

#Min/Max changes:
sorted_changes = sorted(changes_log, key = lambda x: x[1])
date_least, amnt_least = sorted_changes[0]
date_most, amnt_most = sorted_changes[-1]

print(date_least, amnt_least)
print(date_most, amnt_most)

#export as text file
output_path = os.path.join("output" , "new.txt")

with open(output_path, 'w', newline='') as txtfile:
    print(n_months)
    print(net_profit)
    print(average_profit_loss)
    print(avg_change)
    print(date_least, amnt_least)
    print(date_most, amnt_most)
    
output_path = "desktop/output.txt"

print(output_path) 
