solution = lambda f: list(sorted(f, key=lambda t: ("".join(["_" if v.isdigit() else v.lower() for v in t]).split("_")[0], int("".join([v if v.isdigit() else " " for v in t]).split()[0]))))
