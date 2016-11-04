# https://www.hackerrank.com/challenges/ctci-making-anagrams
def number_needed(a, b):
    list_a = list(a)
    list_b = list(b)

    hash_a = {}
    for i in list_a:
        if i in hash_a:
            hash_a[i] += 1
        else:
            hash_a[i] = 1

    hash_b = {}
    for i in list_b:
        if i in hash_b:
            hash_b[i] += 1
        else:
            hash_b[i] = 1

    union = set(list_a) | set(list_b)

    diff = 0
    for u in union:
        diff += abs(hash_a.get(u, 0) - hash_b.get(u, 0))

    return diff

a = input().strip()
b = input().strip()

print(number_needed(a, b))
