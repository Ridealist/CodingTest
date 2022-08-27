"""
https://school.programmers.co.kr/learn/courses/30/lessons/42577
"""

def solution(phone_book: list):
    for idx, phone in enumerate(phone_book):
        for i in range(idx):
            if phone_book[i].startswith(phone):
                return False
        for i in range(idx+1, len(phone_book)):
            if phone_book[i].startswith(phone):
                return False
    return True



def solution(phone_book: list):
    phone_book_copy = phone_book.copy()
    for i in range(len(phone_book)):
        poped_phone = phone_book_copy.pop(i)
        


    for idx, phone in enumerate(phone_book):
        for i in range(idx):
            if phone_book[i].startswith(phone):
                return False
        for i in range(idx+1, len(phone_book)):
            if phone_book[i].startswith(phone):
                return False
    return True
