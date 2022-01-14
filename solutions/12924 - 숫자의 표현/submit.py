from math import sqrt

solution = lambda n: sum(
    (d := ((sqrt(8 * n + 4 * x * x - 4 * x + 1) - 1) / 2)).is_integer()
    and d <= n
    for x in range(1, n + 1)
)
