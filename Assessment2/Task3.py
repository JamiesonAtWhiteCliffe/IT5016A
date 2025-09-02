#In this module I will be provided with statements containing various conditions. My objective will be to write Python functions that use control structures to implement the provided conditions
#based on input from another function.
# Age and the states of them
# If someone is 65+ , mark them as old
# If someone is between 50 and 65, mark them middle age
# If someone is 30 to 50, mark them as matured adults
# If someone is 0 to 30, mark them as young
#Defines the Age Order
def AgeOrder(age: int):
    if age > 65: 
        return "You are old."
    elif age > 50 and age <= 65: 
        return "You are middle age."
    elif age > 30 and age <= 50:
        return "You are a matured adult."
    else:
        return "You are young."

# Outputs the AgeOrder
your_age = int(input("Please enter your age:"))
print(AgeOrder(your_age))
