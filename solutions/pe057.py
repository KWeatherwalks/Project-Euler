"""
Square root convergents
Problem 57

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

\sqrt 2 =1+ \frac 1 {2+ \frac 1 {2 +\frac 1 {2+ \dots}}}

By expanding this for the first four iterations, we get:

 1 + \frac 1 2 = \frac  32 = 1.5
 
1 + \frac 1 {2 + \frac 1 2} = \frac 7 5 = 1.4

1 + \frac 1 {2 + \frac 1 {2+\frac 1 2}} = \frac {17}{12} = 1.41666 \dots

1 + \frac 1 {2 + \frac 1 {2+\frac 1 {2+\frac 1 2}}} = \frac {41}{29} = 1.41379 \dots


The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985,
 is the first example where the number of digits in the numerator exceeds the number of 
 digits in the denominator.

In the first one-thousand expansions, 
 how many fractions contain a numerator with more digits than the denominator?
"""

from fractions import Fraction
from math import gcd

previous_number = 1
counter = 0
for _ in range(1_000):

    fraction = Fraction(1 + 1 / (1 + previous_number))
    # print(previous_number, fraction)
    if len(str(fraction.numerator)) > len(str(fraction.denominator)):
        counter += 1

    previous_number = fraction

print(counter)
