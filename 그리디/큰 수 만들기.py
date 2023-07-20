def solution(number, k):
    k =  len(number)-k
    answer = ''
    for i in range(k):
        if '9' in number[0:-k+1]:
            m = '9'
        else:
            m = max(number) if k==1 else max(number[0:-k+1])
        answer+=m
        number = number[number.find(m)+1:]
        k-=1
    return answer
