def solution(phone_book):
    hash_map = {}
    for phone_num in phone_book:
        for i in range(len(phone_num)):
            hash_map[phone_num[0:i]] = 1
    for phone_num in phone_book:
        if phone_num in hash_map:
            return False
    return True