from collections import deque, defaultdict

def solution(sales, links):
    count = [0] * (len(sales) + 1)
    parent = [-1] * (len(sales) + 1)
    child = defaultdict(list)

    for p, c, in links:
        parent[c - 1] = p - 1
        count[p - 1] += 1

    q = deque(i for i, v in enumerate(count[:-1]) if v == 0)

    while q:
        i = q.popleft()
        p = parent[i]
        if i in child:
            sumv = sum(npick for _, npick in child[i])
            minv = min(min(pick - npick for pick, npick in child[i]), sales[i])
        else:
            sumv, minv = 0, 0
        child[p].append((sales[i] + sumv, minv + sumv))
        count[p] -= 1
        if count[p] == 0:
            q.append(p)

    return min(child[-1][0])
