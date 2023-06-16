import math

def solution(progresses, speeds):
    wait = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    result = []
    flag = 0
    for i in range(len(wait)):
        if wait[i]>wait[flag]:
            result.append(i-flag)
            flag = i
    result.append(len(wait)-flag)

    return result
print(solution([95, 90, 99, 99, 80, 99]	,[1, 1, 1, 1, 1, 1]	))
