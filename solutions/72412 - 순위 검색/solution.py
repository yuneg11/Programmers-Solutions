from collections import defaultdict
from bisect import insort, bisect_left

table = {
    "cpp": 4, "java": 2, "python": 1,
    "backend": 2, "frontend": 1,
    "senior": 2, "junior": 1,
    "chicken": 2, "pizza": 1,
    "-": 7,
}

def preprocess(rows, is_query=False):
    processed_rows = []

    for row in rows:
        values = [value for value in row.split(" ") if value != "and"]

        score = int(values[-1])
        code = 0

        for value in values[:-1]:
            if is_query:
                code = (code << 3) + (7 - table[value]) # Bit flip
            else:
                code = (code << 3) + table[value]

        processed_rows.append((code, score))

    return processed_rows

def solution(info, query):
    info = preprocess(info)
    query = preprocess(query, is_query=True)

    info_index = defaultdict(list)

    for code, score in info:
        insort(info_index[code], score)

    results = []

    for qcode, qscore in query:
        count = sum(
            len(iscores) - bisect_left(iscores, qscore)
            for icode, iscores in info_index.items()
            if qcode & icode == 0
        )


        results.append(count)

    return results
