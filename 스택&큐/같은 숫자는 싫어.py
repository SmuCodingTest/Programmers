def solution(arr):
    stack = []
    for num in arr:
        if len(stack) == 0:
            stack.append(num)
        elif stack[-1]!=num:
            stack.append(num)
    
    return stack

print(solution([1,1,3,3,0,1,1]))
print(1)