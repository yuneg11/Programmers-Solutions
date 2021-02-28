solution = lambda n, t: n[0] == abs(t) if len(n) == 1 else solution(n[1:], t - n[0]) + solution(n[1:], t + n[0])
