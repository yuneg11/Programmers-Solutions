solution = lambda n: (solution(i) if (i := (n - 1) // 3) else "") + "124"[(n - 1) % 3]
