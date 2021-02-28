def solution(s):
    t = ["0"]
    for v in s:
        if t[-1] == v:
            t.pop()
        else:
            t.append(v)
    return [0, 1][len(t) == 1]
