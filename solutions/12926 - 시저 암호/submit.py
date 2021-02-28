solution = lambda s, n: "".join([chr((ord(v) - [97, 65][v.isupper()] + n) % 26 + [97, 65][v.isupper()]) if v != " " else v for v in s])
