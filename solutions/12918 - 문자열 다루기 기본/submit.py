solution = lambda s: (len(s) == 4 or len(s) == 6) and sum(map(lambda x: ord("0") <= ord(x) <= ord("9"), s)) == len(s)
