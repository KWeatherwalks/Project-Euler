# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:22:44 2018
Project Euler
Problem #27 - Quadratic primes
@author: kweatherwalks
"""

def is_prime(n, prime_set):
  if n in prime_set:
    return True
  else: 
    return False

def sieve_of_eratosthenes(max_integer):
    sieve = [True for _ in range(max_integer + 1)]
    sieve[0:1] = [False, False]
    for start in range(2, max_integer + 1):
        if sieve[start]:
            for i in range(2 * start, max_integer + 1, start):
                sieve[i] = False
    primes = []
    for i in range(2, max_integer + 1):
        if sieve[i]:
            primes.append(i)
    return primes
  
"""
  def sieve_of_eratosthenes(max_number):
  number_list = set(range(2,max_number))
  
  prime = number_list.pop()
  number_list.add(prime)
  for p in range(prime, math.ceil(math.sqrt(max_number))):
    prime = number_list.pop()
    number_list.add(prime)
    nonprimes = set(range(prime**2,max_number,prime))
    number_list = number_list.difference(nonprimes)
  
  return number_list
  """

'''
def sieve_of_eratosthenes(limit):
  limitn = limit+1
  not_prime = set()
  primes = []
  
  for i in range(2, limitn):
    if i in not_prime:
      continue
    
    for f in range(i*2, limitn, i):
      not_prime.add(f)
      primes.append(i)
      
  return primes
'''


# Main method
r = 1601
set_of_primes = set(sieve_of_eratosthenes(2*r**2 + r))
max_prime_list = []
coeffs = []

possible_b = set(range(-r,r+1)).intersection(set_of_primes)

# track time elapsed
import time
start_time = time.time()

# run algorithm
for a in range(-r+1, r):
  for b in possible_b:
    primes = []
    n = 0
    while (n < b and is_prime(n**2+a*n+b, set_of_primes)):
      primes.append(n**2+a*n+b)
      n+=1
    if len(primes) > len(max_prime_list):
      coeffs = [a, b]
      max_prime_list = primes

# get end_time
time_elapsed = time.time() - start_time

print('# of sieved primes total: ' + str(len(set_of_primes)))
print('# of primes: ' + str(len(max_prime_list)))
print('[a, b] = ' + str(coeffs))
print('primes: ' + str(max_prime_list))
print('a*b = ' + str(coeffs[0]*coeffs[1]))
print('algorithm runtime: ' + str(time_elapsed) + ' seconds')