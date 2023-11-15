"""
Написать функцию, которая получает на вход список строк.
Функция должна возвращать самый длинный общий для этих строк префикс.

Пример 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

func_name = "longest_common_prefix"

user_code_example = """
def longest_common_prefix(array):
    ans=""
    array=sorted(array)
    first=array[0]
    last=array[-1]
    for i in range(min(len(first),len(last))):
        if(first[i]!=last[i]):
            return ans
        ans+=first[i]
    return ans
"""


def longest_common_prefix(array: list):
    pass


test_cases = [
    ((["flower", "flow", "flight"],), "fl"),
    ((["dog", "racecar", "car"],), ""),
    ((["", ""],), "")
]
