def addition_numbers(num1:int, num2:int)-> int:
    return num1 + num2


def subtractions(num1: int, num2:int) -> int:
    return num1 - num2

def call_other_functions(num1: int, num2: int):
    calculate_value = addition_numbers(num1, num2)
    return calculate_value

a = call_other_functions(5, 9)
print("The calculated value is:",a)