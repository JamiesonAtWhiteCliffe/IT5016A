#This module requires me to demonstrate my ability to call other functions and display their results.
#Defines the multiply calculation
def multiply(num1:int, num2:int)-> int:
    return num1 * num2

#Defines the divide calculation
def divide(num1: int, num2:int) -> int:
    if num2 == 0:
       raise ValueError("You cannot divide by Zero")
    return num1 / num2
    

#Calls the other functions
def call_other_functions(num1: int, num2: int):
    calculate_value = multiply(num1, num2)
    return calculate_value

#Defines the number and prints out the calculation
a = call_other_functions(5, 9)
print("The calculated value is:",a)

