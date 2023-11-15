"""
Написать функцию, которая принимает строку, которая состоит из слов разделенных пробелами.
Функция должна возвращать длину последнего слова в строке.
"""

func_name = "length_of_last_word"

user_code_example = """
def length_of_last_word(text: str):
    return len(text.split()[-1])
"""


def length_of_last_word(text: str):
    return text.split()[-1]


test_cases = [
    (("Hello World",), 5),
    (("   fly me   to   the moon  ",), 4),
    (("luffy is still joyboy",), 6)
]
