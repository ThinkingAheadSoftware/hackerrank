import numpy as np


class LargestPrimeFactor:
    """
    Implement the crieve of erastones
    """
    def __init__(self):
        max = 10**9
        self.primeArray = np.ones(max+1, dtype=bool)
        self.SieveOfEratosthenes(max)

    def SieveOfEratosthenes(self, limit):
        """
        Finding all primes from 0 until limit
        """
        self.primeArray[0] = False
        self.primeArray[1] = False
        self.primeArray[2] = True
        self.primeArray[4::2] = False
        for i in xrange(3, limit+1, 2):
            if(self.primeArray[i]):
                self.primeArray[i**2::2*i] = False

    def getLargestPrimeFactor(self, limit):
        """
        For a give number, find the largest Prime Factor
        """
        upperLimit = int(limit ** (0.5)) + 1

        for i in xrange(upperLimit, 0, -1):
            if (limit % i == 0):
                if(self.primeArray[limit / i]):
                    return limit / i
                elif (self.primeArray[i]):
                    return i

        return limit


def gpf(n):
    divisor = 2
    while n > 1:
        if not n % divisor:
            n /= divisor
            divisor -= 1
        divisor += 1
    return divisor


def main():

    # T = int(raw_input())
    primes = LargestPrimeFactor()
    # for i in xrange(T):
    for i in xrange(1000000000000, 0, -1):
        # nLimit = int(raw_input())
        nLimit = i
        print "i[{1}]={0}".format(primes.getLargestPrimeFactor(nLimit), nLimit)

if __name__ == "__main__":
    main()



# def isPrime(N):
#     for i in range(2, int(N **(0.5))+1):
#         if N % i == 0:
#             return False
#     return True

# T = int(input())
# while T > 0:
#     T = T - 1
#     N = int(input())
#     large = 0
#     i = 2
#     while i <= int(N**(0.5)):
#         while N % i == 0:
#             N = N // i
#             large = i
#         i = i + 1
#     if isPrime(N):
#         large = N
#     print(large)
