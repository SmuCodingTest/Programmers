def solution(s):
    stack = []
    for elem in s:
        if elem == '(':
            stack.append('(')
        elif len(stack)==0:
            return False
        else:
            stack.pop()
    return len(stack)==0
