tri = lambda n: tri(u[0]) + str(u[1]) if (u := divmod(n, 3))[0] else str(u[1])
solution = lambda n: int("".join(list(reversed(tri(n)))), 3)
