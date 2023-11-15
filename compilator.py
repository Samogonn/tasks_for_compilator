# Для тестирования определенной задачи, нужно импортировать ее
# from testing.your_task import func_name, user_code_example, test_cases
from testing.count_prime_numbers import func_name, user_code_example, test_cases
from solution import Solution


solution_instance = Solution(func_name, user_code_example, test_cases)

solution_instance.run_tests()
