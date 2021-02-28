import heapq

def solution(n, times):
    ratio = list(map(lambda x: 1 / x, times))
    ratio_sum = sum(ratio)
    dist = list(map(lambda x: int(n * x / ratio_sum), ratio))
    total = [(t * (d + 1), t) for t, d in zip(times, dist)]
    heapq.heapify(total)

    for _ in range(n - sum(dist)):
        v = heapq.heappop(total)
        heapq.heappush(total, (v[0] + v[1], v[1]))

    m = max(total, key=lambda x: x[0] - x[1])
    return m[0] - m[1]
