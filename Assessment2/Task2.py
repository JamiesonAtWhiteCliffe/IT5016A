#This module is to illustrate my ability to write functions that can perform mathematical computations, call other function(s), and return a value.
#Defines the addition calculation
def addition_numbers(num1:int, num2:int)-> int:
    return num1 + num2

#Defines the subtraction calculation
def subtractions(num1: int, num2:int) -> int:
    return num1 - num2

#Calls the other functions
def call_other_functions(num1: int, num2: int):
    calculate_value = addition_numbers(num1, num2)
    return calculate_value

#Defines the number and prints out the calculation
a = call_other_functions(5, 9)
print("The calculated value is:",a)