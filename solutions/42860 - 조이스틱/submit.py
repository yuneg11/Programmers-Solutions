from itertools import takewhile, chain

solution = lambda n: sum(d := [min(ord("Z") - ord(v) + 1, ord(v) - ord("A")) for v in n]) + len(n) - max(map(lambda l: len(list(takewhile(lambda x: not x, l[0]))) - l[1], chain(((n[i+1:] + n[:i], i) for i in range(len(n))), reversed([(d[i+1:] + d[:i], i) for i in range(len(d))])))) - 1
