"""
Highly divisible triangular number
Euler project 12

See the instructions in pdf file
"""
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


def highly_divisible_triangular(number, prime_array):
    """
    Receive a number to find the highly divisible triangular number.
    """
    counter = 0
    i = 2
    dn1 = 1
    dn2 = 1
    while counter <= number:
        if i % 2 == 0:
            dn2 = prime_factorisation(i+1, prime_array)
            counter = dn2 * dn1
            # print "i%2[{4}]={2} * {3} = {0} < {1}".format(counter, number, dn1, dn2, i+1)
        else:
            dn1 = prime_factorisation((i+1)/2, prime_array)
            counter = dn2 * dn1
            # print "i%2[{4}]={2} * {3} = {0} < {1}".format(counter, number, dn1, dn2,(i+1)/2)
        i += 1

    return i * (i - 1) / 2


def main():
    prime_array = sieve_erast(75000)
    ntests = int(raw_input())
    for i in xrange(ntests):
        ndivisors = int(raw_input())
        print highly_divisible_triangular(ndivisors, prime_array)

if __name__ == "__main__":
    main()
