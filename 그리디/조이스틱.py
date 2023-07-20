def solution(name):
    names = list(name)
    targets = [i for i in range(len(name)) if name[i] != 'A']
    if not targets:
        return 0
    distances = [targets[i + 1] - targets[i] for i in range(len(targets) - 1)]
    distances.append(len(names) - targets[-1]+targets[0])
    print("[targets] ",targets)
    print("[distances] ",distances)
    count = 0
    answers = []
    left = distances.index(max(distances))
    right = (distances.index(max(distances)) + 1) % len(targets)
    print("left :",left,"right :",right)
    answers.append(2 * targets[left] + (len(names) - targets[right]))
    answers.append(len(names)-targets[0])
    answers.append(targets[-1])
    answers.append(2 * (len(names) - targets[right]) + targets[left])
    print()
    print("[answers]",answers)
    count+=min(answers)
    print("[movement]",count)
    for curl in targets:
        count += min(abs(91 - ord(names[curl])), abs(ord(names[curl]) - 65))


    return count

print(solution("AAA"))
