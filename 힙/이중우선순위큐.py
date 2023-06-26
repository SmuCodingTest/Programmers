import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    answer = []
    for s in operations:

        if s[0] == "I":
            answer.append(int(s[2:]))
            heapq.heappush(min_heap,int(s[2:]))
            heapq.heappush(max_heap,(-1*int(s[2:]),int(s[2:])))
        else:
            if s[2]=='1' and max_heap:
                e = heapq.heappop(max_heap)[1]
                while max_heap and e not in answer:
                    e = heapq.heappop(max_heap)[1]
                if answer:
                    answer.remove(e)
            elif min_heap:
                e = heapq.heappop(min_heap)
                while min_heap and e not in answer:
                    e = heapq.heappop(min_heap)
                if answer:
                    answer.remove(e)

    if max_heap and min_heap:
        return [max(answer),min(answer)]
    else:
        return [0,0]
