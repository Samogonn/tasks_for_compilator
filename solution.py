import json
import inspect


class Solution:
    """
    Класс для хранения и обработки пользовательского решения.
    Можно хранить и запускать в компиляторе.
    Можно хранить в тестинге. Отпаравлять в компилятор json,
    сформированный с помощью функции to_json и запускать в компиляторе.
    """
    def __init__(self, func_name: str, user_code: str, test_cases: list[tuple]) -> None:
        self.func_name = func_name
        self.user_code = user_code
        self.test_cases = test_cases

    def run_tests(self):
        try:
            user_namespace = {}
            exec(self.user_code, user_namespace)

            if self.func_name not in user_namespace:
                raise Exception(f"Function {self.func_name} is not defined in the user's code.")

            total_tests = len(self.test_cases)
            passed_tests = 0

            for i, (input_params, expected_output) in enumerate(self.test_cases):
                result = user_namespace[self.func_name](*input_params)
                if result == expected_output:
                    passed_tests += 1
                    print(f"Test case {i + 1} passed. Got: {result}, Expected: {expected_output}")
                else:
                    print(f"Test case {i + 1} failed. Got: {result}, Expected: {expected_output}")

            print(f"Passed tests: {passed_tests}/{total_tests}")
            return passed_tests, total_tests

        except Exception as e:
            print(f"Test execution failed: {e}")
            return 0, 0

    def to_json(self):
        class_source = inspect.getsource(Solution)
        return json.dumps({
            "class_source": class_source,
            "user_code": self.user_code,
            "test_cases": self.test_cases
        })

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(data["user_code"], data["test_cases"])
