def solution(phone_book):
    answer = True
    phone_book.sort()
    for prev, cur in zip(phone_book, phone_book[1:]):
        if cur.startswith(prev):
            answer = False
            return answer
    return answer