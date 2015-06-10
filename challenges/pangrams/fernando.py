import string


def pangram(s):

    for i in list(string.lowercase):
        if i not in s.lower():
            return "not pangram"
    return "pangram"


def main():
    sentence = raw_input()

    print "{0}".format(pangram(sentence))

if __name__ == "__main__":
    main()
