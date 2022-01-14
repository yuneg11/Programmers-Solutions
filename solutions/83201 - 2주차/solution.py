def split_self_score(i, ith_scores):
    self_score = ith_scores[i]
    other_scores = ith_scores[:i] + ith_scores[i+1:]

    return self_score, other_scores


def is_self_score_valid(self_score, other_scores):
    min_score = min(other_scores)
    max_score = max(other_scores)

    return self_score >= min_score and max_score >= self_score


def get_grade(average_score):
    if average_score >= 90:
        return "A"
    elif average_score >= 80:
        return "B"
    elif average_score >= 70:
        return "C"
    elif average_score >= 50:
        return "D"
    else:
        return "F"


def solution(scores):
    scores_transpose = zip(*scores)
    grades = []

    for i, ith_scores in enumerate(scores_transpose):
        self_score, other_scores = split_self_score(i, ith_scores)

        if is_self_score_valid(self_score, other_scores):
            average_score = sum(ith_scores) / len(ith_scores)
        else:
            average_score = sum(other_scores) / len(other_scores)

        grade = get_grade(average_score)
        grades.append(grade)

    return "".join(grades)
