import sys
import heapq

N = int(input())
nums = []
for i in range(N):
    tmp = list(map(int,sys.stdin.readline().split()))
    for num in tmp:
        heapq.heappush(nums,num)
    while len(nums)>N:
        heapq.heappop(nums)

print(heapq.heappop(nums))
