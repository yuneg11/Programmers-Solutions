from functools import reduce

solution = lambda n, h: reduce(lambda y, z: (y[0] + "L", z + y[1][2:]) if z[1] == 0 else (y[0] + "R", y[1][:2] + z) if z[1] == 2 else (y[0] + "L", z + y[1][2:]) if (c := abs(z[0] - y[1][0]) + abs(z[1] - y[1][1])) < (d := abs(z[0] - y[1][2]) + abs(z[1] - y[1][3])) else (y[0] + "R", y[1][:2] + z) if c > d else (y[0] + "L", z + y[1][2:]) if h == "left" else (y[0] + "R", y[1][:2] + z), (divmod(v - 1, 3) if v > 0 else (3, 1) for v in n), ["", (3, 0, 3, 2)])[0]
