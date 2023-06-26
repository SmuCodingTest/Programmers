import heapq
import sys

N = int(input())
ans = []
data = {}
heap_key = []
for i in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        if heap_key:
            key = heapq.heappop(heap_key)
            ans.append(heapq.heappop(data[key]))
            if data[key]:
                heapq.heappush(heap_key,key)
            else:
                del data[key]
        else:
            ans.append(0)
    elif abs(n) in data:
        heapq.heappush(data[abs(n)],n)
    else:
        data[abs(n)] = [n]
        heapq.heappush(heap_key,abs(n))
    N-=1

for num in ans:
    print(num)
