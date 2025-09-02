# This module is to demontrate my knowledge of using Python input methods and the generating of unique ID numbers
# Name: Travis

# Declare a global variable
initial_id = int(input("Please enter your initial ID: "))

#Define a function to generate next Unique ID
def NextUniqueID():
    global initial_id
    initial_id += 1

    uniqueid = initial_id
    return uniqueid

# Call the function and assign the unique ID to the variable uniqueid 
uniqueid = NextUniqueID()

#Output the uniqueid 
print("The Unique ID is: ",uniqueid)
   