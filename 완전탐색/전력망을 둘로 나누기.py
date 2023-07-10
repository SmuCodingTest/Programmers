from collections import deque

def solution(n, wires):
    answer = []

    for cut in wires:
        left = []
        right = []
        left.append(cut[0])
        right.append(cut[1])
        que = deque(wires)
        while que:
            wire = que.popleft()
            if wire == cut:
                continue
            elif wire[0] in left:
                left.append(wire[1])
            elif wire[1] in left:
                left.append(wire[0])
            elif wire[0] in right:
                right.append(wire[1])
            elif wire[1] in right:
                right.append(wire[0])
            else:
                que.append(wire)
        answer.append(abs(len(left)-len(right)))

    return min(answer)
