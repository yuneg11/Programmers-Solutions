solution = lambda n, a, b: [str(bin(c | d))[2:].zfill(n).replace("1", "#").replace("0", " ") for c, d in zip(a, b)]
