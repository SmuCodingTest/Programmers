def solution(money):
    n = len(money)

    f1 = [0 for i in range(n)]
    f2 = [0 for i in range(n)]
    arr = [0]+money[:n-1]
    f1[0] = 0
    f1[1]=arr[1]
    for i in range(2,n):
        f1[i] = max(f1[i-1],f1[i-2]+arr[i])
    print(arr,f1)
    arr = [0]+money[1:n]
    f2[0] = 0
    f2[1]=arr[1]
    for i in range(2,n):
        f2[i] = max(f2[i-1],f2[i-2]+arr[i])
    print(arr,f2)
    return max(f1[n-1],f2[n-1])

print(solution([1, 2, 3, 1]))
