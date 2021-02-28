def solution(play, adv, logs):
    c = lambda t: int(t[0:2]) * 3600 + int(t[3:5]) * 60 + int(t[6:8])
    play, adv = c(play), c(adv)
    logs = sorted([s for t in logs for s in [(c(t[:8]), 1), (c(t[9:]), 0)]])

    v, p, b = 0, 0, [0] * play
    for t, m in logs:
        if v > 0:
            b[p:t] = [v] * (t - p)
        v, p = v + (1 if m else -1), t

    mv, mi = (s := sum(b[:adv]), 0)
    for i, j in zip(range(play - adv), range(adv, play)):
        s += b[j] - b[i]
        if s > mv:
            mv, mi = s, i + 1

    return f"{mi//3600:02d}:{mi%3600//60:02d}:{mi%60:02d}"
