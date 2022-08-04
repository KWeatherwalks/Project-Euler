"""
Powerful digit sum
Problem 56

A googol (10100) is a massive number: one followed by one-hundred zeros;
100100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, 
    what is the maximum digital sum?
"""


def digitsum(n):
    return sum([int(s) for s in str(n)])


current_max = 0

for a in range(100):

    for b in range(100):

        current_max = max(digitsum(a**b), current_max)

print(current_max)
