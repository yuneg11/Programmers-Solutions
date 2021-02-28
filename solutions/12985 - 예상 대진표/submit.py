from math import log2

def solution(e, a, b, s=1):
    a, b, m1, m2 = min(a, b), max(a, b), (s + e) // 2, (s + e) // 2 + 1
    if s <= a <= m1 and m2 <= b <= e:
        return int(log2(e - s + 1))
    else:
        return solution(*((m1, a, b, s) if s <= a <= b <= m1 else (e, a, b, m2)))
