"""
Написать функцию, которая принимает список чисел и целое число.
Функция должна возвращать индексы двух чисел, сумма которых равна двум.
Предпологается, что существует только одно решение.
"""

func_name = "sum_of_two"

user_code_example = """
def sum_of_two(nums, target):
    numToIndex = {}
    for i in range(len(nums)):
        if target - nums[i] in numToIndex:
            return [numToIndex[target - nums[i]], i]
        numToIndex[nums[i]] = i
    return []
"""


def sum_of_two(nums, target):
    numToIndex = {}
    for i in range(len(nums)):
        if target - nums[i] in numToIndex:
            return [numToIndex[target - nums[i]], i]
        numToIndex[nums[i]] = i
    return []


test_cases = [
    (([2, 7, 11, 15], 9), [0, 1]),
    (([3, 2, 4], 6), [1, 2]),
    (([3, 3], 6), [3, 3])
]
