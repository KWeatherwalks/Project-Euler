"""
Project Euler Problem 58
Spiral primes
Starting with 1 and spiralling anticlockwise in the following way, 
 a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal,
 but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; 
 that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above,
 a square spiral with side length 9 will be formed. 
If this process is continued, 
 what is the side length of the square spiral for which
 the ratio of primes along both diagonals first falls below 10%?
"""
from sympy.ntheory import isprime

# new idea: generate diagonal values and check if they are prime
#  track count of primes along with count of non-primes


if __name__ == "__main__":

    from time import time

    start_time = time()

    primes = nonprimes = 0

    side_length = 1

    while (not nonprimes) or (primes / (nonprimes + primes) > 0.10):

        for i in range(1, 5):

            number = side_length**2 + i * (side_length + 1)

            if isprime(number):
                primes += 1
            else:
                nonprimes += 1

        side_length += 2

    padding_length = 25
    print(
        f"{'side length':<25}{side_length:>25}",
        f"{'prime:composite':<25}{primes/nonprimes:>25.4f}",
        f"{'largest number in square':<25}{side_length**2:>25,}",
        f"{'number of primes':<25}{primes:>25,}",
        f"{'<10% ?':<25}{primes / (primes+nonprimes) <= 0.1:>25}",
        f"completed in {time() - start_time:.1f} seconds",
        sep="\n",
    )
