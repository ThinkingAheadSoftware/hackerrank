# This solution has a timeout
# def ransom_note(magazine, rasom):
#     for r in rasom:
#         if r not in magazine:
#             return False
#         else:
#             magazine.remove(r)
#     return True


def ransom_note(magazine, rasom):
    from collections import Counter
    return Counter(rasom) - Counter(magazine) == {}

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
