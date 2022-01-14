from collections import deque, defaultdict

def get_far(graph, startv):
    q, maxv, maxw = deque([(startv, 0, -1)]), [], 0

    while q:
        curv, curw, fromv = q.popleft()

        if curw > maxw:
            maxv, maxw = [curv], curw
        elif curw == maxw:
            maxv.append(curv)

        for nv in graph[curv]:
            if nv != fromv:
                q.append((nv, curw + 1, curv))

    return maxv, maxw

def solution(n, edges):
    graph = defaultdict(list)
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    v2s, _ = get_far(graph, v1)
    v3s, w = get_far(graph, v2s[0])

    if len(v3s) > 1:
        return w
    v4s, _ = get_far(graph, v3s[0])
    return w if len(v4s) > 1 else w - 1
