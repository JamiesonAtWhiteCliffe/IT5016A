def multiply(num1:int, num2:int)-> int:
    return num1 * num2

def divide(num1: int, num2:int) -> int:
    if num2 == 0:
       raise ValueError("You cannot divide by Zero")
    return num1 / num2
    


def call_other_functions(num1: int, num2: int):
    calculate_value = multiply(num1, num2)
    return calculate_value

a = call_other_functions(5, 9)
print("The calculated value is:",a)

