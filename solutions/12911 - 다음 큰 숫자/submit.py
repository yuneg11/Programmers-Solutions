solution = lambda n: int(s := bin(n + int(bin(2 ** (len(b := bin(n)) - b.rindex("1") - 1)), 2)), 2) + int("1" * (sum(map(int, b[2:])) - sum(map(int, s[2:]))) or "0", 2)
