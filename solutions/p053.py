# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 12:17:15 2018
Project Euler
Problem 53 - Combinatoric selections
@author: kweatherwalks
"""

import math

def nCr(n,r):
  return math.factorial(n)//(math.factorial(r) * math.factorial(n-r))


def num_trailing_zeros(n):
  i = 1
  count = 0
  while (math.floor(n/5**i)>0):
    count += math.floor(n/5**i)
    i += 1
  return count

def is_greater_than_million(n,k):
  N = num_trailing_zeros(n)
  K = num_trailing_zeros(k)
  Nk = num_trailing_zeros(n-k)
  
  if N-K-Nk>5:
    return True
  else:
    return False

