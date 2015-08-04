# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import ceil

def sum_three_five(number):
    total = 0
    total += sum(xrange(3,number,3))
    total += sum(xrange(5,number,5))
    total -= sum(xrange(15,number,15))

    sum_3 = ((1 + ((number - 1) / 3)) / 2.0) * ceil((number - 1) // 3) * 3;
    sum_5 = ((1 + ((number - 1) / 5)) / 2.0) * ceil((number - 1) // 5) * 5;
    sum_15 = ((1 + ((number - 1) / 15)) / 2.0) * ceil((number - 1) // 15) * 15;
    total2 = int(sum_3 + sum_5 - sum_15)

    print "{0} {1}".format(total, total2)

    return total


def main():
    T = int(raw_input())
    for i in xrange(T):
        n = int(raw_input())
        print "{0}".format(sum_three_five(n))


if __name__ == "__main__":
    main()
