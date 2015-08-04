from math import log, sqrt

golden = (1 + sqrt(5)) / 2.0

def sum_even_fib(n):
    sumfib = 0
    a, b = 0, 1
    while b < n:
        if b % 2 == 0:
            sumfib = sumfib + b
        a, b = b, a + b
    return sumfib


def inverse_fibonacci(fiboNumber):
    if(fiboNumber <= 0):
        return 0
    elif(fiboNumber == 1):
        return 1

    # result = int(log(fiboNumber * sqrt(5.0), golden) + 1/2)
    # Floor@N@Log[GoldenRatio, (fn Sqrt[5] + Sqrt[5 fn^2 - 4])/2]
    result = int(log((fiboNumber * sqrt(5) + sqrt(5 * fiboNumber**2 -4)) / 2.0, golden))
    
    #print result
    return result

def sum_even_fibonacci(k):
    phi = golden**3
    psi = -golden**(-3)
    #        (1 / Sqrt[5]) * (phi * ((1 - phi^k )/(1 - phi)) - psi*((1 - psi^k )/(1 - psi)))
    result = (1 / sqrt(5)) * (phi * ((1 - phi**k)/(1 - phi)) - psi*((1 - psi**k)/(1 - psi)))
    
    return int(result)




def main():
    nTest = int(raw_input())
    for i in xrange(nTest):
        limit = int(raw_input())
        print "{0}".format(sum_even_fib(limit))
        n = inverse_fibonacci(limit)
        print "{0}".format(sum_even_fibonacci(n/3))

if __name__ == "__main__":
    main()