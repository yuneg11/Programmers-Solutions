class s(str): __lt__ = lambda a, b: a + b > b + a

solution = lambda n: str(int("".join(sorted(map(s, n)))))
