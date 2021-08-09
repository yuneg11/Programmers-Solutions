def solution(board):
    m, d = 0, [0] * (len(board[0]) + 1)

    for r, p in zip(board, [0] * len(board)):
        m = max(m, max(d := [0] + [(p := min(a, b, p) + 1 if v else 0) for a, b, v in zip(d[:-1], d[1:], r)]))

    return m * m
