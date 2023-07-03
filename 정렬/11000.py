import heapq
import sys

N = int(input())
data = []
for i in range(N):
    data.append(tuple(map(int,sys.stdin.readline().split())))

data.sort(key = lambda x : x[0])

heap_list = []
for i in range(N):
    if not heap_list:
        heap_list.append(data[i][1])

    else:
        tmp = []
        if heap_list[0]<=data[i][0]:
            heapq.heappop(heap_list)
            heapq.heappush(heap_list,data[i][1])
        else:
            heapq.heappush(heap_list,data[i][1])


print(len(heap_list))
