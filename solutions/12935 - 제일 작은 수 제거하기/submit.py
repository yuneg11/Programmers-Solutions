solution = lambda a: d if (m := min(a)) and (d := [v for v in a if v != m]) else [-1]
