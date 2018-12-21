basic_salary = float(input("Enter Your  Salary : "))
class employee:
    def salary(self):
        self.taxes=basic_salary*0.35
        self.cell_phone_expences=basic_salary*0.05
        self.food_expences=basic_salary*0.10
        self.transpotation_expences=basic_salary*0.10
        self.clothing_expences=basic_salary*0.05
        self.medical_expences=basic_salary*0.03
        self.total_expences=self.taxes+self.cell_phone_expences+self.food_expences+self.transpotation_expences+self.clothing_expences+self.medical_expences
        self.savings=basic_salary-self.total_expences
    def display(self):
        print("Your Monthly Salary : ",basic_salary)
        print("Taxes :" ,self.taxes)
        print("Cellphone :" ,self.cell_phone_expences)
        print("Food :" ,self.food_expences)
        print("Transpotation:" ,self.transpotation_expences)
        print("Clothing:" ,self.clothing_expences)
        print("Medical:" ,self.medical_expences)
        print("Total:" ,self.total_expences)
        print("Savings:" ,self.savings)
#calling block
emp=employee()
emp.salary()
emp.display()




