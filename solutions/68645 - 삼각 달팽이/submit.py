def solution(n):
    a, x, y, c = [[0 for _ in range(i + 1)] for i in range(n)], -1, 0, 0

    for i in range(n, 0, -1):
        for j in range(i):
            x, y = (x + 1, y) if (n - i) % 3 == 0 else (x, y + 1) if (n - i) % 3 == 1 else (x - 1, y - 1)
            a[x][y] = (c := c + 1)

    return [v for b in a for v in b]
