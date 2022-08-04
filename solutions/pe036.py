# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 11:25:57 2018
Project Euler
Problem 36 - Double-base palindromes
@author: kweatherwalks
"""


def decimal_palindrome(max_num):
  pals = set()
  for num in range(1,max_num+1):
    
    if str(num) == str(num)[::-1]:
      pals.add(num)
  
  return pals

def binary_palindrome(max_num):
  bpals = set()
  for decimal_number in range(1,max_num+1):
    
    if '{0:b}'.format(decimal_number) == '{0:b}'.format(decimal_number)[::-1]:
      bpals.add(decimal_number)
  
  return bpals

dec_pals = decimal_palindrome(10**6)
bin_pals = binary_palindrome(10**6)

sum_of_pals = 0
for number in dec_pals.intersection(bin_pals):
  sum_of_pals += number

print(sum_of_pals)