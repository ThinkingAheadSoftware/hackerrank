from math import sqrt
from itertools import count, islice


def isPrime(n):
    if n < 2:
        return False
    return all(n % i for i in islice(count(2), int(sqrt(n)-1)))


def gpf(limit):
    upperLimit = int(limit ** (0.5)) + 1
    for i in xrange(upperLimit, 0, -1):
        if (limit % i == 0):
            if isPrime(limit / i):
                return limit / i
            elif isPrime(i):
                return i
    return limit


def main():

    T = int(raw_input())
    for i in xrange(T):
        upper = int(raw_input())
        print "{0}".format(gpf(upper))

if __name__ == "__main__":
    main()
