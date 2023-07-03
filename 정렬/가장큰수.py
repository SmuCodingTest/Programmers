numbers = [0,0]
from functools import cmp_to_key

def mysort(x,y):
    return -1 if int(str(x)+str(y))>int(str(y)+str(x)) else 1

def solution(numbers):
    answer = ""
    for number in sorted(numbers, key = cmp_to_key(mysort)):
        answer+=str(number)

    return str(int(answer))
print(sorted(numbers, key = cmp_to_key(mysort)))
print(solution(numbers))
