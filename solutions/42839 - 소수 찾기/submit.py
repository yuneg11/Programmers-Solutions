from itertools import permutations
from math import sqrt, ceil

def prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    else:
        return all(number % i != 0 for i in range(2, ceil(sqrt(number)) + 1))

def solution(numbers):
    answer = 0

    check = set()

    for w in range(1, len(numbers) + 1):
        for r in permutations(numbers, w):
            number = int("".join(r))
            if number not in check:
                check.add(number)
                if prime(number):
                    answer += 1

    return answer
