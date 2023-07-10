import time

def solution(word):
    words = ['A','E','I','O','U']
    answer = []
    for c in word:
        answer.append(words.index(c))

    count = 0
    current = []

    while current != answer:
        if not current:
            current.append(0)
        elif current[-1]==5:
            current.pop()
            current[-1]+=1
            count-=1
        elif len(current)<5:
            current.append(0)
        else:
            current[-1]+=1
        count+=1
        print(current,count)
        # time.sleep(0.5)
    return count

solution("I")
