import heapq

def solution(scoville, K):
    min_heap = []
    for item in scoville:
      heapq.heappush(min_heap, item)

    for i in range(len(scoville)):
        e = heapq.heappop(min_heap)
        if(e>=K):
                return i
        if min_heap:
            heapq.heappush(min_heap,e+(heapq.heappop(min_heap)*2))
            print(min_heap)

    return -1

print(solution([1, 2, 3, 9, 10, 12],7))
