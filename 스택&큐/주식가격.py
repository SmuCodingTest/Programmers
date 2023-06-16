from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        e = prices.popleft()
        count = 0
        for price in prices:
            count+=1
            if e>price:
                break

        answer.append(count)
    return answer


