from datetime import date
counter = 1000
# Created a Python function called staff_info. I used Python input methods to collect information about
#  a staff member submitting a requisition (i.e, Date. Staff ID, Staff Name and Requisition ID).
#A unique ID should be generated using a counter plus 10000 and assigned as the requisition ID.
def staff_info():
    today = date.today()
    staff_id = input("Please enter staff id: ")
    staff_name = input("Please enter your staff name: ")
    global counter
    counter += 1
    requisition_id = counter

    # This function should return all inputs and the requisition ID.
    return [today, requisition_id, staff_id, staff_name]

    
