from heapq import heappop as pop, heappush as push

def solution(scoville, K):
    answer = 0
    h = []

    for v in scoville:
        push(h, v)

    while len(h) > 0:
        low = pop(h)

        if low >= K:
            return answer
        elif len(h) > 0:
            push(h, low + pop(h) * 2)
            answer += 1

    return -1
