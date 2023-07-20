import heapq

def solution(n, costs):
    heap = []

    visited = [0 for i in range(n)]
    edges = {node: [] for node in range(n)}

    for v1, v2, cost in costs:
        edges[v1].append((v2, cost))
        edges[v2].append((v1, cost))


    print('[edges]', edges)
    heapq.heappush(heap,(0,0))
    sum = 0

    while heap:

        cost,v = heapq.heappop(heap)
        if visited[v]:
            continue
        sum +=cost
        visited[v]=1

        for w, cost in edges[v]:
            if not visited[w]:
                heapq.heappush(heap,(cost,w))

        print(v,sum,heap,visited)
    return sum
print(solution(7, [[2, 3, 7], [3, 6, 13], [3, 5, 23], [5, 6, 25], [0, 1, 29], [1, 5, 34], [1, 2, 35], [4, 5, 53], [0, 4, 75]]))
