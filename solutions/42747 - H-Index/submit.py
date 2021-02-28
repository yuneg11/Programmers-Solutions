def solution(citations):
    h = 0
    for i, v in enumerate(sorted(citations, reverse=True)):
        if v >= i + 1:
            h = i + 1
        else:
            return h
    return h
