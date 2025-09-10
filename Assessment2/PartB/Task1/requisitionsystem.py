from datetime import date


class RequisitionSystem:
    requisition_count = 10000 
    requisition_repository = []

    def   __init__(self) -> None:
        RequisitionSystem.requisition_count += 1
        self.requisition_date = date.today()
        self.requisition_id = RequisitionSystem.requisition_count
        self.staff_id = ""
        self.staff_name = ""
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approve_reference = ""
        RequisitionSystem.requisition_repository.append(self)

    
    def staff_info(self):
        self.staff_id = input("Please enter your staff id: ")
        self.staff_name = input("Please enter your staff name: ")
    
    
    def requisition_details(self):
        while True:
            item_name = input("Please enter your requisition item: ")
            if item_name.lower() == "done":
                break
            item_price = int(input("Please enter your item price: "))
            self.items.append((item_name, item_price))
            self.total += item_price

    
    def requisition_approval(self):
        if self.status == "Pending":
            l = len(self.items)
            if l > 0:
                if self.total < 500:
                    self.status = "Approved"
                    self.approve_reference = self.staff_id + str(self.requisition_id)[-3:]
                
                    
    def respond_requisition(self):
        if self.status == "Pending":
            l = len(self.items)
            if l > 0:
                if self.total >= 500:
                    status = input("Please enter your decision to approve or decline the requisition: ")
                    if status.lower() == "approved":
                        self.status == "Approved"
                        self.approve_reference = self.staff_id + str(self.requisition_id)[-3:]
                    else:
                        self.status = "Not Approved"


    @staticmethod
    def display_requisitions():
        for requisition in RequisitionSystem.requisition_repository:
            print("Date:", requisition.requisition_date)
            print("Requisition ID:", requisition.requisition_id)
            print("Staff ID:", requisition.staff_id)
            print("Staff Name:", requisition.staff_name)
            print("Total:", requisition.total)
            print("Status:", requisition.status)
            print("Approval Reference Number:", requisition.approve_reference)

    @staticmethod
    def requisition_statistic():
        approved_count = 0
        not_approved_count = 0
        pending_count = 0
        for requisition in RequisitionSystem.requisition_repository:
            if requisition.status == "Approved":
                approved_count += 1
            elif requisition.status == "Pending":
                pending_count += 1
            else: 
                not_approved_count += 1
        print("Total Number of requisitions submitted", len(RequisitionSystem.requisition_repository))
        print("Total Number of approved requisitions", approved_count)
        print("Total Number of pending requisitions", pending_count)
        print("Total Number of not approved requisitions", not_approved_count)




requisition_1 = RequisitionSystem()
requisition_1.staff_info()
requisition_1.requisition_details()
requisition_1.requisition_approval()
requisition_1.respond_requisition()

requisition_2 = RequisitionSystem()
requisition_2.staff_info()
requisition_2.requisition_details()
requisition_2.requisition_approval()
requisition_2.respond_requisition()

requisition_3 = RequisitionSystem()
requisition_3.staff_info()
requisition_3.requisition_details()
requisition_3.requisition_approval()
requisition_3.respond_requisition()

requisition_4 = RequisitionSystem()
requisition_4.staff_info()
requisition_4.requisition_details()
requisition_4.requisition_approval()
requisition_4.respond_requisition()

RequisitionSystem.display_requisitions()
RequisitionSystem.requisition_statistic()

