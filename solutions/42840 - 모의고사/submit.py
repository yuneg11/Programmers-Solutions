from itertools import cycle

def solution(answers):
    p1 = cycle([1, 2, 3, 4, 5])
    p2 = cycle([2, 1, 2, 3, 2, 4, 2, 5])
    p3 = cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    c = [[0, 1], [0, 2], [0, 3]]

    for a, *r in zip(answers, p1, p2, p3):
        for i in range(3):
            if a == r[i]:
                c[i][0] += 1

    c.sort(reverse=True)

    answer = []

    for v, i in c:
        if v == c[0][0]:
            answer.append(i)
        else:
            break

    return sorted(answer)
