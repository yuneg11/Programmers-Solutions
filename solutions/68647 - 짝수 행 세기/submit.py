cache = dict()

def c(n, k, a=1, b=1):
    if (key := str(f"{n},{k}")) in cache:
        return cache[key]
    else:
        for i in range(min(n - k, k)):
            a, b = a * (i + 1), b * (n - i)
        cache[key] = (result := b // a)
        return result

def solution(a):
    s, dp = [sum(v) for v in zip(*a)], [0] * ((l := len(a)) + 1)
    dp[s[0]] = c(l, s[0])

    for v in s[1:]:
        prev, dp = dp, [0] * (l + 1)
        for u in range(v + 1):
            for e, k in enumerate(prev):
                if k and 0 <= (f := e + v - u * 2) <= l and 0 <= e - u <= l - v:
                    dp[f] = (dp[f] + c(e, u) * c(l - e, v - u) * k) % 10000019

    return dp[0]
