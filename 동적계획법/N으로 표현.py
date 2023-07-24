def solution(N, number):
    answer = 1
    dp = [[]]
    while (answer <= 8):
        new = []
        sum = 0
        for i in range(answer):
            sum = sum * 10 + N
        new.append(sum)
        for i in range(1, answer):
            for n1 in dp[i]:
                for n2 in dp[answer - i]:
                    new.append(n1 + n2)
                    new.append(n1 - n2)
                    new.append(n1 * n2)
                    if n2 !=0:
                        new.append(n1 // n2)
        if number in new:
            return answer
        else:
            dp.append(new)
            print(answer,dp[answer])
            answer += 1

    return -1


print(solution(5, 12))
