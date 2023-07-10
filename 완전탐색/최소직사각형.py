def solution(sizes):
    max_size = []
    min_size = []
    for size in sizes:
        max_size.append(max(size))
        min_size.append(min(size))

    return max(max_size)*max(min_size)
