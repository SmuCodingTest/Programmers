import heapq
import sys

T = int(input())
for i in range(T):
    N = int(input())
    data = []
    for i in range(N):
        data.append(tuple(map(int,sys.stdin.readline().split())))

    data.sort(key = lambda x : x[0])

    count = 0
    min_heap = []
    for i in range(N):
        if not min_heap:
            count+=1
        elif data[i][1]<min_heap[0]:
            count+=1
        heapq.heappush(min_heap,data[i][1])
    print(count)
