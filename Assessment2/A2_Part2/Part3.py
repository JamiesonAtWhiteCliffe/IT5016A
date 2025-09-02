from Part2 import requisitions_total

def requisition_approval():
    requisition = requisitions_total()
    status = ""
    approval_reference = ""
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
