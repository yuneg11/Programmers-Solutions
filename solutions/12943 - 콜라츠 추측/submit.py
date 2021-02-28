def solution(n):
    for i in range(501):
        if n == 1:
            return i
        else:
            n = n * 3 + 1 if n % 2 else n // 2
    return -1
