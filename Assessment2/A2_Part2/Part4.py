from Part3 import requisition_approval
#Create a Python function called display_requisitions. 
# The function should display the staff's basic information and the total of his requisition.
def display_requisitions():
    requi = requisition_approval()
    print("Date: ", requi[0])
    print("Requisition ID: ", requi[1])
    print("Staff ID: ", requi[2])
    print("Staff Name: ", requi[3])
    print("Total: ", f"${requi[4]:,.0f}")
    print("Status: ", requi[5])
    print("Approval Reference Number: ", requi[6])



display_requisitions()