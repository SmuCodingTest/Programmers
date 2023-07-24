def cal(num1,num2,op):
    num1 = int(num1)
    num2 = int(num2)
    if op == "+":
        return num1+num2
    else:
        return num1-num2

def solution(arr):
    max_dp = [[-100000 for j in range(202)] for i in range(202)]
    min_dp = [[100000 for j in range(202)] for i in range(202)]
    for step in range(0,len(arr),2):
        for i in range(0,len(arr)-step,2):
            start = i
            end = i+step
            print("F[",start,"][",end,"]")
            if start == end:
                min_dp[start][end] = int(arr[start])
                max_dp[start][end] = int(arr[start])
            else:
                for i in range(0,end-start,2):
                    if arr[start+i+1] == "+":
                        print("=> F[",start,"][",start+i,"]",arr[start+i+1],"F[",start+i+2,"][",end,"]")
                        max_dp[start][end] = max(max_dp[start][end],max_dp[start][start+i]+max_dp[start+i+2][end])
                        min_dp[start][end] = min(min_dp[start][end],min_dp[start][start+i]+min_dp[start+i+2][end])
                    else:
                        print("=> F[",start,"][",start+i,"]",arr[start+i+1],"F[",start+i+2,"][",end,"]")
                        max_dp[start][end] = max(max_dp[start][end],max_dp[start][start+i]-min_dp[start+i+2][end])
                        min_dp[start][end] = min(min_dp[start][end],min_dp[start][start+i]-max_dp[start+i+2][end])
            # print("DP[",start,"][",end,"]",dp[start][end])
    return max_dp[0][len(arr)-1]


print(solution(["1", "-", "3", "+", "5", "-", "8"]))
