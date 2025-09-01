# Age and the states of them
# If someone is 65+ , mark them as old
# If someone is between 50 and 65, mark them middle age
# If someone is 30 to 50, mark them as matured adults
# If someone is 0 to 30, mark them as young
def AgeOrder(age: int):
    if age > 65: 
        return "You are old."
    elif age > 50 and age <= 65: 
        return "You are middle age."
    elif age > 30 and age <= 50:
        return "You are a matured adult."
    else:
        return "You are young."


your_age = int(input("Please enter your age:"))
print(AgeOrder(your_age))
