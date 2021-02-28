# 순위 검색

| ID | 난이도 | 제목 | 분류 | 링크 | 언어 |
| -- | ---- | :-- | :-- | --- | --- |
| 72412 | Level 2 | 순위 검색 | 2021 KAKAO BLIND RECRUITMENT | [문제](https://programmers.co.kr/learn/courses/30/lessons/72412) | [![javascript](/assets/javascript.svg)](solution.js) [![python3](/assets/python3.svg)](solution.py) |

| 언어 | short | solution | submit |
| --- | ----- | -------- | ------ |
| JavaScript | [submit.js](submit.js) (same) | [solution.js](solution.js) | [submit.js](submit.js) |
| Python3 | [submit.py](submit.py) (same) | [solution.py](solution.py) | [submit.py](submit.py) |

<br>
<br>

## 접근

문제에서 원하는 바는 `query`의 각 원소 `q`에 대해서 `info`에 만족하는 원소 `i`가 몇 개 있는지 구하는 것입니다. 이를 다음과 같이 가장 무식한 방법으로 푼다고 생각해 봅시다.

<br>

### 무식한 방법

```python
for q in query:
    for i in info:
        if i satisfies q:
            count += 1
```

답을 구하기 위해서는 `query`에 존재하는 모든 `q`에 대해서 `info`에 존재하는 모든 `i`를 확인해야 합니다. 그러면 `info`의 길이가 N이고 `query`의 길이가 M일 때, 시간 복잡도는 `O(N x M)`이 됩니다. 문제 제한 사항에서 `N = 50,000`이고 `M = 100,000`라고 주어졌으므로 `for`문이 최대 `5,000,000,000`번 실행되어야 하므로 적절하지 않은 것 같습니다.

<br>

### `info` 범위 줄이기

`query`의 각 조건에 대해서 `info`의 모든 원소를 검사하는 것은 비효율적으로 보입니다. 그러면 `info`를 구조화해서 `info`의 필요 없는 부분은 검사하지 않도록 합니다.

**1. `조건` 구조화 하기**

먼저 `조건`에 해당하는 모든 경우의 수를 계산해 봅시다.
- 개발언어: 3개 (`cpp`, `java`, `python`)
- 직군: 2개 (`backend`, `frontend`)
- 경력구분: 2개 (`junior`, `senior`)
- 소울푸드: 2개 (`chicken`, `pizza`)

`3 x 2 x 2 x 2 = 24`개 이므로 구조화 하기 적절해 보입니다. 이를 구조화 해봅시다.

```python
index = dict(contains list) # {key: value} = {condition: [scores]}
for i in info:
    index[condition].push(score)
```

`info`의 각 원소는 `24`개 부분 집합 중에서 하나의 부분 집합에만 포함 됩니다. `24`개의 리스트에 `info`에 포함된 최대 `50,000`개의 원소가 중복 없이 분배되므로 메모리 관리 측면에서 적절해 보입니다. 다만 `query`에는 모든 항목을 의미하는 `-`가 포함되어 있으므로 `query`의 각 원소에 대해 만족하는 모든 `조건`들을 알아내기 위해서는 최대 `24`개 리스트를 전부 순회해야 할 수 있습니다. 그러면 `query`의 관점에서 구조화를 다시 진행해봅시다.

```python
index = dict(contains list) # {key: value} = {condition: [scores]}
for i in info:
    index[condition00].push(score) # condition = a, b, c, d
    index[condition01].push(score) # condition = -, b, c, d
    index[condition02].push(score) # condition = a, -, c, d
    ...
    index[condition14].push(score) # condition = a, -, -, -
    index[condition15].push(score) # condition = -, -, -, -
```

이제 부분 집합의 개수는 `4 x 3 x 3 x 3 = 108`개 입니다. `info`의 각 원소는 `108`개 부분 집합 중에서 여러 부분 집합에 중복해서 포함될 수 있습니다. `108`개의 리스트에 최대 `50,000`개의 원소가 `2^4 = 16`번 중복해서 분배되므로 최대 `50,000 x 16 = 800,000`개의 원소를 메모리에 저장해야 합니다. `800,000`개 정도면 크게 무리한 메모리 사용량은 아닌 것 같습니다. 따라서 나중에 상황을 보고 시간과 메모리 중에서 더 효율적으로 사용해야 할 자원에 따라 방법을 선택하면 될 것 같습니다.

**2. `점수` 구조화 하기**

문제의 조건에서 `점수`의 범위가 `1` 이상 `100,000` 이하라고 주어졌으므로 `점수`에 따라서 `x`점 이상인 `info`의 원소들을 포함하는 부분 집합들로 구조화 할 수 있습니다.

```python
index = dict(contains list) # {key: value} = {score: [conditions]}
for i in info:
    for score in (1 to 100000):
        index[score].push(condition)
```

하지만 최악의 경우 `sigma(x, 1 ~ 50,000) + 50,000 x 50,000 = 3,750,025,000`개의 중복된 원소를 메모리에 저장해야 하고, 실제 사용된 점수만 구조화 한다고 하더라도 최대 `sigma(x, 1 ~ 50,000) = 1,250,025,000`개의 중복된 원소를 메모리에 저장해야 합니다. 더 최적화를 할 방법이 있을지 모르겠지만 위 `1`번 방법과 비교하여 더 고민할 이유는 없어 보입니다.

<br>
<br>

## 구현

`조건`을 구조화하는 방법을 사용하기로 하였으므로, 아까 미뤄두었던 세부 사항을 결정할 때입니다. `조건`을 `info`의 관점에서 구조화 하는 방법이 있었고, `query`의 관점에서 구조화 하는 방법이 있었습니다. 이를 간단히 정리하면 다음과 같습니다. (`조건`의 경우의 수 `C`, `info`의 길이 `N`)

- `info`의 관점에서 `info` 구조화
  - 시간 복잡도: `O(C x N)`
  - 공간 복잡도: `O(N)`
- `query`의 관점에서 `info` 구조화
  - 시간 복잡도: `O(N)`
  - 공간 복잡도: `O(C x N)`

사실 이 문제에서 주어진 제한 사항 안에서는 두 방법 다 사용 가능합니다. 만약 이 문제가 더 높은 난이도의 문제였다면 어떨까요? 저는 아마 `N`에 대한 제한 사항을 더 어렵게 줄 것 같습니다. `조건`을 확인하기 위해 순회하는 시간을 줄이는 방법은 있지만 메모리 사용량을 줄이는 방법은 당장은 떠오르지 않는 것 같습니다. 그래서 저는 `info`의 관점에서 `info`를 구조화 하는 전자의 방법을 선택하도록 하겠습니다.

<br>

### 조건 확인

두 조건이 주어졌을 때 같은 조건인지 확인하려면 어떻게 해야 할까요? 간단하게는 다음과 같이 할 수 있을 것 같습니다.

```python
a = ["cpp", "frontend", "junior",  "pizza" ]
b = [ "-" , "frontend",    "-"  , "chicken"]

if a[0] == b[0] or b[0] == "-":
    if a[1] == b[1] or b[1] == "-":
        if a[2] == b[2] or b[2] == "-":
            if a[3] == b[3] or b[3] == "-":
                return true

return false
```

직관적이고 간단합니다. 하지만 문자열 비교는 시간을 좀 더 사용하게 만들고 있습니다. 전처리를 해서 숫자로 바꾸겠습니다.

```python
table = {
    "cpp": 1, "java": 2, "python": 3,
    "backend": 1, "frontend": 2,
    "senior": 1, "junior": 2,
    "chicken": 1, "pizza": 2,
    "-": 0,
}

a = [1, 2, 2, 2] # ["cpp", "frontend", "junior",  "pizza" ]
b = [0, 2, 0, 1] # [ "-" , "frontend",    "-"  , "chicken"]

if a[0] == b[0] or b[0] == 0:
    if a[1] == b[1] or b[1] == 0:
        if a[2] == b[2] or b[2] == 0:
            if a[3] == b[3] or b[3] == 0:
                return true

return false
```

숫자 비교를 통해 약간의 시간 최적화를 진행했습니다. 사실 이 정도까지만 진행해도 상관 없을 것 같습니다. 하지만 여전히 `조건`이 배열에 들어있고, 각각의 원소를 비교해야 합니다. 여러 조건문을 하나로 줄일 수 있을까요? 이제 `bit field`와 `bit mask`를 사용해 봅시다. ([Wikipedia](https://en.wikipedia.org/wiki/Bit_field))

**Bit field**

`bit field`와 `bit mask`를 다음과 같이 정의 합니다. (보편적인 방식과는 다를 수 있습니다.)

```cpp
field = {                     mask = {
    "cpp":      1, /* 001 */      "cpp":      6, /* 110 */
    "java":     2, /* 010 */      "java":     5, /* 101 */
    "python":   4, /* 100 */      "python":   3, /* 011 */

    "backend":  1, /* 001 */      "backend":  6, /* 110 */
    "frontend": 2, /* 010 */      "frontend": 5, /* 101 */

    "senior":   1, /* 001 */      "senior":   6, /* 110 */
    "junior":   2, /* 010 */      "junior":   5, /* 101 */

    "chicken":  1, /* 001 */      "chicken":  6, /* 110 */
    "pizza":    2, /* 010 */      "pizza":    5, /* 101 */

    "-":        7, /* 111 */      "-":        0, /* 000 */
}
```

그러면 이제 `bit field`와 `bit mask`가 어떻게 동작하는지 몇 가지 예시를 살펴보겠습니다.

- `cpp field` and `cpp mask`:  `1 & 6 = 001 & 110 = 000 = 0`
- `cpp field` and `java mask`: `1 & 5 = 001 & 101 = 001 = 1`
- `cpp field` and `- mask`:    `1 & 0 = 001 & 000 = 000 = 0`
- `frontend mask` and `frontend mask`: `2 & 5 = 010 & 101 = 000 = 0`
- `frontend mask` and `backend mask`:  `2 & 6 = 010 & 110 = 010 = 2`
- `frontend mask` and `- mask`:        `2 & 0 = 010 & 000 = 000 = 0`

다음과 같이 두 `조건`이 만족하면 계산 결과가 `0(000)`이고, 아니면 `0` 이상의 값이 나옴을 알 수 있습니다. 그러면 조건 전체를 `bit field`로 표현해 보겠습니다.

```js
  a   = 001 010 010 010 = 658 // ["cpp", "frontend", "junior",  "pizza" ]
  b   = 000 101 000 110 = 326 // [ "-" , "frontend",    "-"  , "chicken"]
a & b = 000 000 000 010 =   2 // [ true,    true   ,   true  ,   false  ]
```

위의 예시에서는 소울푸드 항목에서 두 조건이 달랐기 때문에 0이 나오지 않았지만, 모든 조건이 같으면 계산 결과가 0이 나올 것이라는걸 알 수 있습니다. 의사코드로 구체화하면 다음과 같습니다.

```python
a = ["cpp", "frontend", "junior",  "pizza" ]
b = [ "-" , "frontend",    "-"  , "chicken"]

a_bit = (field[a[0]] << 9) + (field[a[1]] << 6) + (field[a[2]] << 3) + field[a[3]]
b_bit = ( mask[b[0]] << 9) + ( mask[b[1]] << 6) + ( mask[b[2]] << 3) +  mask[b[3]]

return a & b == 0
```

이제 조건문 없이 두 조건이 만족하는지 여부를 알 수 있게 되었습니다. 따라서 `24`개의 `info` 부분 집합 중에서 관심을 가져야 할 부분 집합을 구하려면 `24`번의 비트 연산을 수행하면 됩니다.

<br>

### 점수 확인

추가 예정
