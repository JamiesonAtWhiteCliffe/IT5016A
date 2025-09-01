initial_id = int(input("Please enter your initial ID: "))

#Define a function to generate next Unique ID
def NextUniqueID():
    global initial_id
    initial_id += 1

    uniqueid = initial_id
    return uniqueid

uniqueid = NextUniqueID()
print("The Unique ID is: ",uniqueid)
   