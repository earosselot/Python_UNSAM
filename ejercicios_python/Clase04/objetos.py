# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 11:35:33 2021

@author: Eduardo
"""

import csv

f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

types = [str, float, tuple, str, float, float, float, float, int]
row[2] = [ int(num) for num in row[2].split('/') ]
converted = [ func(val) for func, val in zip(types, row) ]
record = dict(zip(headers, converted))
