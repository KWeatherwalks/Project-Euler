# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 19:11:13 2019

@author: kweat
"""
import math

fact = [1];
for i in range(1,10):
  fact.append(fact[i-1]*i)

def factorialSum(n):
  sum = 0
  while n>0:
    sum += fact[n%10]
    n = math.floor(n/10)
    
  return sum

def solution():
  sum = 0
  for i in range(10,1500000):
    if i == factorialSum(i):
      sum += i
  
  return sum

