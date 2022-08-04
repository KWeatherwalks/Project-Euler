# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 12:17:15 2018
Project Euler
Problem 625 - Gcd Sum
@author: kweatherwalks
"""

import math, time, numpy as np

def modK(n):
  if n > 998244353:
    return n % 998244353
  else:
    return n

def sieve_of_eratosthenes(max_integer):
    sieve = [True for _ in range(max_integer + 1)]
    sieve[0:1] = [False, False]
    for start in range(2, max_integer + 1):
        if sieve[start]:
            for i in range(2 * start, max_integer + 1, start):
                sieve[i] = False
    primes = np.zeros(max_integer)
    num_primes = 0
    for i in range(2, max_integer + 1):
        if sieve[i]:
            primes[num_primes] = i
            num_primes += 1
    return primes[:max_integer]

def gcd_sum(N):
  Gsum = 0
  list_of_primes = sieve_of_eratosthenes(N)
  
  # start at 2 since gcd(1,1)=1
  for j in range(2,N+1):
    if j in list_of_primes:
      Gsum += j-2
    else:
      for i in range(2,j):
        Gsum += math.gcd(i,j)
    Gsum += j+1
    Gsum = modK(Gsum)
    
  return Gsum+1 # to account for gcd(1,1)

start_time = time.time()
print(gcd_sum(10**4))
time_elapsed = time.time() - start_time
print('time elapsed: ' + str(time_elapsed))