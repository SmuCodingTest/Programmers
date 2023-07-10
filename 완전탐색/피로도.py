from itertools import permutations

def solution(k, dungeons):
    cases = list(permutations(dungeons,len(dungeons)))
    answer = []
    for case in cases:
        tmp = k
        answer.append(0)
        for dungeon in case:
            if tmp < dungeon[0]:
                break
            else:
                answer[-1]+=1
                tmp -= dungeon[1]
    return max(answer)
