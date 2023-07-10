import math

def solution(brown, yellow):
    total = brown + yellow
    divisors = []
    for i in range(1,int(math.sqrt(total))+1):
        if total%i==0:
            divisors.append((total//i,i))

    for divisor in divisors:
        if 2*(divisor[0]+divisor[1])-4 == brown:
            return [divisor[0],divisor[1]]
