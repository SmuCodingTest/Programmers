
def solution(triangle):
    height = 2
    dp = [[],[7]]
    triangle = triangle[1:]
    print(triangle)
    for nums in triangle:
        dp.append([])
        print("height",height,nums)
        for i in range(len(nums)):
            left = right = -1
            if i-1 >= 0:
                print(nums[i],"+",dp[height-1][i-1],"(left)")
                left = dp[height-1][i-1]

            if i<len(dp[height-1]):
                print(nums[i],"+",dp[height-1][i],"(right)")
                right = dp[height-1][i]
            dp[height].append(nums[i]+max(left,right))
        height+=1
        print()
    print(dp)
    return max(dp[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	))
