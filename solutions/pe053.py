# Project Euler Problem 53
# Combinatoric selections

# loop over all n from 23 to 100

# find when the threshold is met and add to count remaining unchecked

from math import comb

counter = 0

for n in range(23, 101):
  r = 1
  while comb(n, r) < 1_000_000:
    r += 1
  if n % 2 == 0:
    counter += 2*(n/2-r)+1
  else:
    counter += 2*(n//2-r)+2

print(int(counter))
