def solution(n):
    a = [False, False] + [True for i in range(2, n + 1)]
    for i in range(2, n // 2 + 1):
        if a[i]:
            for j in range(i * 2, n + 1, i):
                a[j] = False
    return sum(a)
