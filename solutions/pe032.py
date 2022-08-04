# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 11:25:57 2018
Project Euler
Problem 32 - Pandigital products
@author: kweatherwalks
"""
import itertools

def subsets_of_size_n(l, n):
  list_of_subsets = []
  for digit in itertools.product(l, repeat = n):
    list_of_subsets.append(''.join(digit))
  return list_of_subsets

def one_by_four_pandigital():
  digits = '123456789'
  list_of_subsets = subsets_of_size_n(digits,5)
  pandigital_products = []
  
  for combo in list_of_subsets:
    
    product = int(combo[0]) * int(combo[1:])
    digits_used = combo + str(product)
    unused_digits = set(digits).difference(set(digits_used))
    
    if len(digits_used) == 9 and len(unused_digits) == 0:
      pandigital_products.append([combo, product])
      
  return pandigital_products

def two_by_two_pandigital():
  digits = '123456789'
  list_of_subsets = subsets_of_size_n(digits,4)
  pandigital_products = []
  
  for combo in list_of_subsets:
    
    product = int(combo[:2]) * int(combo[2:])
    digits_used = combo + str(product)
    unused_digits = set(digits).difference(set(digits_used))
    
    if len(digits_used) == 9 and len(unused_digits) == 0:
      pandigital_products.append([combo, product])
      
  return pandigital_products

def two_by_three_pandigital():
  digits = '123456789'
  list_of_subsets = subsets_of_size_n(digits,5)
  pandigital_products = []
  
  for combo in list_of_subsets:
    
    product = int(combo[:2]) * int(combo[2:])
    digits_used = combo + str(product)
    unused_digits = set(digits).difference(set(digits_used))
    
    if len(digits_used) == 9 and len(unused_digits) == 0:
      pandigital_products.append([combo, product])
      
  return pandigital_products

list_of_products = set()
for item in one_by_four_pandigital():
  list_of_products.add(item[1])
  print(item[0][:1] + ' * ' + item[0][2:] + ' = ' + str(item[1]))
for item in two_by_two_pandigital():
  list_of_products.add(item[1])
  print(item[0][:2] + ' * ' + item[0][3:] + ' = ' + str(item[1]))
for item in two_by_three_pandigital():
  list_of_products.add(item[1])
  print(item[0][:2] + ' * ' + item[0][2:] + ' = ' + str(item[1]))

sum_of_products = 0
for product in list_of_products:
  sum_of_products += product

print(sum_of_products)