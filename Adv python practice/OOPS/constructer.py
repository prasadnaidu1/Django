class sample:
    comp_name = "Sathya technologies"
    comp_adds = "Hyderabad"
    def __init__(self):
        while True:
            try:
                self.employee_id = int(input("Enter a No : "))
                self.employee_name = input("Enter a Name : ")
                print("Company Name : ",sample.comp_name)
                print("Company Adds : ",sample.comp_adds)
                print("Employee Id : ", self.employee_id)
                print("Employee Name : ", self.employee_name)
            except:
                print("invalid input")
            ans=input("To Continue Press y : ")
            if ans=="y" or ans=="Y":
                continue
            else:
                break


    def display(self):
        pass
#calling block
s1 = sample()
s1.display()







