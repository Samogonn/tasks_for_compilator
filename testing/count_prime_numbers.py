"""
Написать функцию, которая принимает натуральное число num.
Функция должна возвращать количество простых чисел,
которые встречаются в диапазоне до num включительно.
"""

func_name = "count_prime_numbers"

user_code_example = """
def count_prime_numbers(num: int) -> int:
    count = 0
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count += 1
    return count
"""


test_cases = [
    ((3, ), 2),
    ((0,), 0),
    ((99,), 25),
    ((-13,), 0)
]


def count_prime_numbers(num: int) -> int:
    pass


print(count_prime_numbers(-13))
