# https://www.hackerrank.com/challenges/ctci-balanced-brackets

# list = ['{', '[', '(', ')', ']', '}']
# stack = []
# { take element from list
# look if stack is empty, if it is, push element
# list = [[', '(', ')', ']', '}']
# stack = [{]
# [ next element, check if it is its counterpart
# stack = [{,[]
# ( next element. check ..
# stack = [{,[,(]
# ) next element, check. It is. Pop element from stack
# stack = [{,[]
# ] next, check, it is. Pop element
# stack = [{]
# } next, check, it is. pop element
# stack is empty? and stack is empty? True, else False
#
#
# take the first element (opening bracket) and verify if its counterpart is the first in the stack
# while is opening brackets do the push operation
# if the element taken from list matches its counterpart on the stack, pop element from stack
# else if the element is a closing bracket but it's not from the same type return error
# else
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
