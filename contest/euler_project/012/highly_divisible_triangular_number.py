"""
Highly divisible triangular number
Euler project 12

See the instructions in pdf file
"""

import math
from ctypes import c_ubyte


def sieve_erast(upper_limit):
    """
    Receive a upper limit and find all primes under this value.
    """
    sieve_bound = int(upper_limit - 1) / 2
    # define the number of odd numbers to analyse
    # example, if upper_sqrt is 4, refers to list [3,5,7,9]
    upper_sqrt = (int(upper_limit**0.5) - 1) / 2

    # using a bit_array to save memory (only for the odd values)
    bit_array = (c_ubyte * (sieve_bound + 1))()

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


def prime_factorisation(number, prime_array):
    """
    Find the number of divisions using prime factorisation.
    """
    ndivisors = 1
    expoent = 0
    remain = number

    for i in prime_array:
        if i ** 2 > number:
            return ndivisors * 2

        expoent = 1

        while remain % i == 0:
            expoent += 1
            remain /= i

        ndivisors *= expoent

        if remain == 1:
            return ndivisors

    return ndivisors


# def divisors_n(n, start):
#     if n == 1:
#         return 1
#     for i in xrange(start, int(math.ceil(math.sqrt(n)))+1):
#         if n % i == 0:
#             cnt = 1
#             while n % i == 0:
#                 n /= i
#                 cnt += 1
#             return divisors(n, i+1) * cnt
#     return 2

# def divisors(n):
#     number_of_factors = 0
#     for i in xrange(1, int(math.ceil(math.sqrt(n)))+1):
#         if n % i == 0:
#             number_of_factors +=2
#         if i*i==n:
#             number_of_factors -=1
#     return number_of_factors

# def pFactors(n):
#         """Finds the prime factors of 'n'"""
#         from math import sqrt
#         pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n
#         if n == 1: return [1]
#         for check in range(2, limit):
#              while num % check == 0:
#                 pFact.append(check)
#                 num /= check
#         if num > 1:
#           pFact.append(num)
#         return pFact

# for i in range(1,1000):
#         print pFactors(i)

# def max(limit):
#     for n in xrange(1, 1000000):
#         Tn = (n*(n+1)) / 2
#         if n % 2 == 0:
#             cnt = divisors(n/2) * divisors(n+1)
#         else:
#             cnt = divisors(n) * divisors((n+1)/2)
#         if cnt >= limit:
#             return ((1 + n) * n) / 2


def main():
    prime_array = sieve_erast(75000)
    counter = 0
    i = 2
    dn1 = 2
    dn2 = 2
    while counter < 500:
        if i % 2 == 0:
            dn2 = prime_factorisation(i+1, prime_array)
            counter = dn2 * dn1
        else:
            dn1 = prime_factorisation((i+1)/2, prime_array)
            counter = dn2 * dn1
        i += 1

    print i * (i - 1) / 2
    # print prime_factorisation(500, prime_array)


if __name__ == "__main__":
    main()
