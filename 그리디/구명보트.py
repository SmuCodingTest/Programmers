from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    sum = 0
    while(people):
        while(people):
            person = people.pop()
            if sum+person>limit:
                people.append(person)
                break
            else:
                sum+=person
        while(people):
            person = people.popleft()
            if sum+person>limit:
                people.appendleft(person)
                break
            else:
                sum+=person
        answer+=1
        sum=0
    return answer
