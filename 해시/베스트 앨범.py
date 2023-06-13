def solution(genres, plays):
    hash_map = { genre:{} for genre in set(genres) }
    rank = {genre:0 for genre in set(genres)}
    result = []
    for i in range(len(genres)):
        hash_map[genres[i]][i]=plays[i]
        rank[genres[i]]+=plays[i]

    ranks = dict(sorted(rank.items(),key=lambda x : x[1], reverse = True))

    for rank in ranks:
        tmp = [e[0] for e in sorted(hash_map[rank].items(),key=lambda x : x[1], reverse = True)]
        result += tmp[0:min(len(hash_map[rank]),2)]

    return result