from math import sqrt, modf

solution = lambda n: -1 if (d := modf(sqrt(n)))[0] else (d[1] + 1) ** 2
