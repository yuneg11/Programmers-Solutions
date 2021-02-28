def solution(phone_book):
    for phone_number in phone_book:
        for idx in range(len(phone_number)):
            if phone_number[:idx] in phone_book:
                return False
    return True
