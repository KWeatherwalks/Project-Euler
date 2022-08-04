# -*- coding: utf-8 -*-
"""
Project Euler
Problem 29 - Distinct powers

Created on Fri Apr 20 10:31:13 2018

@author: kweatherwalks
"""

terms = set()

for a in range(2,101):
  for b in range(2,101):
    terms.add(a**b)

print(len(terms))