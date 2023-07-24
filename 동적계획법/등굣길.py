def solution(m, n, puddles):
    dp = [[10000 for i in range(n)] for j in range(m)]
    dp[0][0]=0

    for y in range(n):
        for x in range(m):
            print(dp[x][y],end = " ")
        print()

    for y in range(n):
        for x in range(m):
            print("dp[",x,"][",y,"]")
            if [x+1, y+1] in puddles:
                continue

            #left
            if x-1 >= 0:
                print("dp[",x,"][",y,"] : ",dp[x][y],"dp[",x-1,"][",y,"] : ",dp[x-1][y],"=>",end = " ")
                dp[x][y] = min(dp[x][y],dp[x-1][y]+1)
                print(dp[x][y])
            #up
            if y-1 >= 0:
                print("dp[",x,"][",y,"] : ",dp[x][y],"dp[",x,"][",y-1,"] : ",dp[x][y-1],"=>",end = " ")
                dp[x][y] = min(dp[x][y],dp[x][y-1]+1)
                print(dp[x][y])
    for y in range(n):
        for x in range(m):
            print(dp[x][y],end = " ")
        print()
    return dp[m-1][n-1]-1

print(solution(4,3,[[2, 2]]))
