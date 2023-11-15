"""
Написать функцию, которая принимает целое число.
Возвращает True, если число является полиндромом и Faslse, если нет.
"""


func_name = "is_palindrom"

user_code_example = """
def is_palindrom(num):
    return str(num) == str(num)[::-1]
"""


def is_palindrom(num):
    return str(num) == str(num)[::-1]


test_cases = [
    ((121,), True),
    ((-123,), False),
    ((10,), False)
]
