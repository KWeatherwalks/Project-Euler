# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 10:22:44 2018
Project Euler
Problem #35 - Circular primes
@author: kweatherwalks
"""

def is_circular_prime(rotations, prime_set):
  i = 0
  while i < len(rotations) and rotations[i] in prime_set:
    i+=1
  if i == len(rotations):
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
set_of_primes = set(sieve_of_eratosthenes(10**6))
circular_primes = set()

for p in set_of_primes.difference(circular_primes):
  rotations = []
  num_string = str(p)
  for digit in num_string:
    rotations.append(int(num_string))
    num_string = num_string[len(num_string)-1] + num_string[0:len(num_string)-1]
  
  if is_circular_prime(rotations, set_of_primes):
    for r in rotations:
      circular_primes.add(r)

print(len(circular_primes))
print(circular_primes)