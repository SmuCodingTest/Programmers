from itertools import permutations

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def solution(numbers):
    nums = set()
    answer = []
    for i in range(len(numbers)):
        comb = list(permutations(numbers,i+1))
        for num in comb:
            nums.add(int(''.join(num)))
    for num in nums:
        if is_prime(num):
            answer.append(num)

    return len(answer)
