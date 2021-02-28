solution = lambda n: 1 if n == 1 else solution(n - 1) + 1 if n % 2 else solution(n // 2)
