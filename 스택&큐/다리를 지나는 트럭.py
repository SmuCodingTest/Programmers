from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    wait = deque([[w,0] for w in truck_weights])
    progress = deque()
    cur = 0
    while wait or progress:
        print(answer,progress)
        if progress and progress[0][1]==bridge_length:
            cur-=progress[0][0]
            progress.popleft()
        if wait and cur+wait[0][0] <= weight:
            cur+=wait[0][0]
            progress.append(wait.popleft())



        answer+=1
        for truck in progress:
            truck[1]+=1

    return answer

print(solution(2,10,[7,4,5,6]))
