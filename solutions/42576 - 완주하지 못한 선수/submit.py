def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
