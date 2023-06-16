from collections import deque

def solution(priorities, location):
    count = 0
    wait_que = deque([(i,p) for i,p in enumerate(priorities)])

    while wait_que:
        elem = wait_que.popleft()
        if any(elem[1] < e[1] for e in wait_que):
            wait_que.append(elem)
        else:
            count+=1
            if elem[0] == location:
                return count

