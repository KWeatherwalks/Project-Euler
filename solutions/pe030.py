# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 10:01:59 2018

@author: kweat
"""

def quintsum(s) :
  """ input a string consisting of 5 digits """
  sum = 0
  for digit in s:
    sum += int(digit)**5
  return sum

numbers = []

# since 6*9^5 < 10^6-1, we only need to look at numbers
# up to 6*9^5 = 354294
for i in range(2, 354295):
  if quintsum(str(i)) == i :
    numbers.append(i)

total = 0
for num in numbers:
  total += num

print(numbers)
print(total)