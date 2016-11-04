# https://www.hackerrank.com/challenges/ctci-balanced-brackets

def is_matched(expression):
    counterparts = {
        '{' : '}', '}' : '{',
        '[' : ']', ']' : '[',
        '(' : ')', ')' : '('
    }

    expression = list(expression)
    stack = []

    if expression:
        stack.append(expression.pop(0))
        for e in expression:
            if not stack:
                stack.append(e)
                continue
            if counterparts[e] == stack[-1]:
                stack.pop()
            else:
                stack.append(e)
    if not stack:
        return True
    else:
        return False

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
