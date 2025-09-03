# Create a Python function called requisitions_total. Calll the function staff_info from Task 1.
# Then ask the staff to input his requisition items (i.e, each item name with a price). 
# This function should return the computed total value for all the requisition items.
from Part1 import staff_info

def requisitions_total():
    requisition = staff_info()

    total = 0
    items = []

    item_name = input("Please enter your requisition item: ")
    item_price = int(input("Please enter your item price: "))
    items.append((item_name, item_price))
    total += item_price

    
    item_name = input("Please enter your requisition item: ")
    item_price = int(input("Please enter your item price: "))
    items.append((item_name, item_price))
    total += item_price

    
    item_name = input("Please enter your requisition item: ")
    item_price = int(input("Please enter your item price: "))
    items.append((item_name, item_price))
    total += item_price

    requisition.append(total)
    return requisition

   # print(f"${total:,.0f}")
