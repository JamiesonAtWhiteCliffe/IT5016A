# This function is built on Tasks 1 & 2. A Python function called requisition_approval is created.
# This function is intended to make approval decisions based on the conditions provided in the 'Responding-
# - to requests' section below.
from Part2 import requisitions_total

def requisition_approval():
    requisition = requisitions_total()
    # This function should use the function requisitions_total (from Task 2) as input.
    status = ""
    approval_reference = ""
    # The default status of all submitted requisitions should be set as "Pending". Once a requisition is approved,
    # the status should change to "Approved".
    # If the Total of a submitted requisition is less than $500, the system should automatically approve the
    #requisition and assign an approval reference number based on the following rule:
    # Staff ID followed by the last three characters of the Requisition ID.
    # If the Total of a submitted requisition is $500 or higher, the program should automatically set the 
    # status to "Pending".

    if requisition[4] < 500 :
        status = "Approved"
        last3_char = str(requisition[1])[-3:]
        approval_reference = requisition[2] + last3_char
    else:
        status = "Pending"


    requisition.append(status)
    requisition.append(approval_reference)
    
    return requisition

requi = requisition_approval()

print("Total", requi[4])
print("Status", requi[5])
print("Approval Reference", requi[6])
