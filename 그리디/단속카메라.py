def solution(routes):
    answer = 0
    routes.sort(key = lambda x:-x[1])
    last_camera = -30001
    while routes:
        cur = routes.pop()
        if cur[0]<=last_camera:
            continue
        else:
            last_camera = cur[1]
            answer+=1
        
    return answer
