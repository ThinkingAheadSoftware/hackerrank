"""
Sieve of Erastosthenes

This algorithm was developed by Erastosthenes in 200 BC.

The input for this algorithm is a upper limit to define the primes to find.

The result is a list with all primes under this limit.

To understand the algorithm, see:
    * wikipidia =
    * http://www.mathblog.dk/sum-of-all-primes-below-2000000-problem-10/
"""

import ctypes
from time import time


def sieve_erast(upper_limit):
    """
    Receive a upper limit and find all primes under this value.
    """
    sieve_bound = int(upper_limit - 1) / 2
    # define the number of odd numbers to analyse
    # example, if upper_sqrt is 4, refers to list [3,5,7,9]
    upper_sqrt = (int(upper_limit**0.5) - 1) / 2

    # using a bit_array to save memory (only for the odd values)
    bit_array = (ctypes.c_ubyte * (sieve_bound + 1))()

    # walk in the odd numers
    for i in xrange(1, upper_sqrt + 1):
        if not bit_array[i]:
            # convert the multiples of odd numbers to correct decimal value
            for j in xrange(i*2*(i+1), sieve_bound, 2*i+1):
                bit_array[j] = 1

    prime_array = [2]
    for i in xrange(1, sieve_bound + 1):
        if not bit_array[i]:
            prime_array.append(2*i + 1)

    return prime_array


def main():
    """
    Main program to test the algorithm
    """
    ncases = int(raw_input())
    start = time()
    sieve_erast(ncases)
    print time() - start

if __name__ == "__main__":
    main()
