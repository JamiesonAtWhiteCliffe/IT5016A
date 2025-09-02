from datetime import date
counter = 1000

def staff_info():
    today = date.today()
    staff_id = input("Please enter staff id: ")
    staff_name = input("Please enter your staff name: ")
    global counter
    counter += 1
    requisition_id = counter

    return [today, requisition_id, staff_id, staff_name]

    
