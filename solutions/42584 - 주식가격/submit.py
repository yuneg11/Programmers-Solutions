def solution(p):
    a, s, l = [0 for _ in range(len(p))], [], len(p)

    for i, v in enumerate(p + [0]):
        while s and s[-1][0] > v:
            _, j = s.pop()
            a[j] = i - j - (l == i)
        s.append((v, i))

    return a
