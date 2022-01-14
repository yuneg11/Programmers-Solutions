def delete(c, p):
    for key in list(c.keys()):
        while len(c[key]) > 0 and c[key][0] < p:
            c[key].pop(0)
        if len(c[key]) == 0:
            del c[key]

def solution(n, k):
    c = dict([[str(i), []] for i in reversed(range(10))])
    for i, v in enumerate(n):
        c[v].append(i)

    delete(c, 0)

    a, l, p = [], len(n), 0
    while k > 0 and k < l - p:
        for key, value in c.items():
            if c[key][0] <= p + k:
                a.append(key)
                k -= value[0] - p
                p = c[key][0] + 1
                delete(c, p)
                break


    return "".join(a) + (n[p:] if k < l - p else "")
