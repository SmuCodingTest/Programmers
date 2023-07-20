def solution(n, lost, reserve):
    clothes = [1 for i in range(n)]
    clothes = [clothes[i]-1 if i+1 in lost else clothes[i] for i in range(n)]
    clothes = [clothes[i]+1 if i+1 in reserve else clothes[i] for i in range(n)]

    for i in range(n):
        if clothes[i]==0 and 0 < i and clothes[i-1]==2:
            clothes[i]+=1
            clothes[i-1]-=1
        elif clothes[i]==0 and i<n-1 and clothes[i+1]==2:
            clothes[i]+=1
            clothes[i+1]-=1
    return len([x for x in clothes if x>0])
