import heapq
from time import sleep

def solution(jobs):
    min_j = []
    min_t = []
    for t,j in jobs:
        heapq.heappush(min_t, (t, j))
    time = 0
    sum = 0
    while min_t or min_j:
        while min_t:

            e_t = heapq.heappop(min_t)
            if e_t[0]<=time:
                heapq.heappush(min_j,(e_t[1],e_t[0]))
            else:
                heapq.heappush(min_t,e_t)
                break
        print(time,min_t,min_j)
        while min_j:
            e_j = heapq.heappop(min_j)
            time+=e_j[0]
            sum += time-e_j[1]
            print(time,min_t,min_j)
        else:
            time+=1
    return(sum//len(jobs))

print(solution([[0, 3], [1, 9], [2, 6]]))
