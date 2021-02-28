from collections import Counter

solution = lambda s: Counter(s.lower())["p"] == Counter(s.lower())["y"]
