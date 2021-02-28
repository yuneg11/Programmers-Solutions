def solution(n, lost, reserve):
    lost_set, reserve_set = set(lost), set(reserve)
    lost_set, reserve_set = lost_set - reserve_set, reserve_set - lost_set
    for r in reserve_set:
        if r-1 in lost_set:
            lost_set.remove(r-1)
        elif r+1 in lost_set:
            lost_set.remove(r+1)
    return n - len(lost_set)
