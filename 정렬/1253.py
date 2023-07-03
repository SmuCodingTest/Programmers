import math
import sys

N = int(input())
data = list(map(int,sys.stdin.readline().split()))
data.sort()

count = 0
for i in range(N):
    left = 0
    right = i-1
    while(left<right):
        sum = data[left]+data[right]
        print(i, left,right,sum, data[i])
        if sum < data[i]:
            left = int(math.floor((left+right)/2))
        elif sum > data[i]:
            right = int(math.floor((left+right)/2))
        else:
            count+=1
            break
print(count)

