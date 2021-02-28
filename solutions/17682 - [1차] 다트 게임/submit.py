def solution(d, c=1, a=[[1, 0, 1] for _ in range(4)]):
    for v in d:
        if v in "SDT": a[c][2], c = {"S": 1, "D": 2, "T": 3}[v], c + 1
        elif v == "#": a[c - 1][0] = -1
        elif v == "*": a[c - 2][0], a[c - 1][0] = a[c - 2][0] * 2, a[c - 1][0] * 2
        else: a[c][1] = a[c][1] * 10 + int(v)
    return sum(map(lambda a: a[0] * (a[1] ** a[2]), a))
