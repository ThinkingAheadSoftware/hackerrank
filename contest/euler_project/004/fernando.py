def find_multiples(num):
    for i in xrange(100, 999):
        if num % i == 0:




def find_palindrome(num):
    for i in xrange(num, 100001, -1):
        str_num = str(i)
        if ((str_num[0] == str_num[5]) and (str_num[1] == str_num[4]) and
                (str_num[2] == str_num[3])):
            return i


def largest_palindrome_product(num):
    while(True):
        palindrome = find_palindrome(num)
        print "{0}".format(palindrome)



def main():
    nCase = int(raw_input())
    for i in xrange(nCase):
        limit = int(raw_input())
        print "{0}".format(largest_palindrome_product(limit))


if __name__ == '__main__':
    main()
