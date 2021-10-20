# 2주차

| ID | 난이도 | 제목 | 분류 | 링크 | 언어 |
| -- | ---- | :-- | :-- | --- | --- |
| 83201 | Level 1 | 2주차 | 위클리 챌린지 | [문제](https://programmers.co.kr/learn/courses/30/lessons/83201) | [![javascript](/assets/javascript.svg)](submit.js) [![python3](/assets/python3.svg)](solution.py) |

| 언어 | short | solution | submit |
| --- | ----- | -------- | ------ |
| JavaScript | - | - | [submit.js](submit.js) |
| Python3 | - | [solution.py](solution.py) | [submit.py](submit.py) |

<br>
<br>

## `python 3` 숏코딩 풀어 쓴 버전

일반적인 `python 3` 풀이는 [`solution.py`](./solution.py)를 참고해 주세요.

```python
def split_self_score(i, ith_scores):
    self_score = ith_scores[i]
    other_scores = ith_scores[:i] + ith_scores[i+1:]

    return self_score, other_scores


def is_self_score_valid(self_score, other_scores):
    min_score = min(other_scores)
    max_score = max(other_scores)

    if min_score <= self_score <= max_score:
        return True
    else:
        return False


def solution(scores):
    scores_transpose = zip(*scores)
    grades = []

    for i, ith_scores in enumerate(scores_transpose):
        self_score, other_scores = split_self_score(i, ith_scores)

        if is_self_score_valid(self_score, other_scores):
            valid_scores = [self_score, *other_scores]
        else:
            valid_scores = other_scores

        average = sum(valid_scores) / len(valid_scores)  # 평균
        tens_place = int(average / 10)         # 10의 자리

        # 10의 자리가 어느 위치인가 확인 (일반적인 풀이에서는 if문으로 처리하는게 맞습니다)
        # (A) 9x ~ 100 -> 5, 6으로   (D) 5x ~ 6x -> 1, 2로
        # (B) 8x       -> 4로        (F) 0x ~ 4x -> 0으로
        # (C) 7x      -> 3으로
        grade_index = max(tens_place - 4, 0)
        grade = "FDDCBAA"[grade_index]
        grades.append(grade)

    return "".join(grades)
```

<br>
<br>

## 저작권

코딩테스트 연습에 공개된 문제는 (주)그렙이 저작권을 가지고 있습니다.

출처: [프로그래머스 코딩 테스트 연습](https://programmers.co.kr/learn/challenges)
