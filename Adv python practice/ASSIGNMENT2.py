basic_salary = float(input("Enter Your  Salary : "))
class employee:
    def salary(self):
        tax=input("If You Have Tax Expenses Press y/Y : ")
        if tax=="y":
            ta=float(input("Enter How much TaxExpenses You Have(In The Form Of Percentage): "))
            ta_r=ta/100
            self.taxes=basic_salary*ta_r
        else:
            self.taxes=0

        cellphone = input("If  Have You CellPhone Expenses Press y/Y : ")
        if cellphone=="y":
            ce=float(input("Enter How much CellPhoneExpenses You Have(In The Form Of Percentage) :"))
            ce_r=ce/100
            self.cell_phone_expences=basic_salary*ce_r
        else:
            self.cell_phone_expences=0

        food = input("If You Have Food Expenses Press y/Y :")
        if food=="y":
            fo = float(input("Enter How much FoodExpenses You Have(In The Form Of Percentage) : "))
            fo_r = fo / 100
            self.food_expences=basic_salary*fo_r
        else:
            self.food_expences=0

        trans=input("If You Have Transpotation Expenses Press y/Y :")
        if trans=="y":
            tr = float(input("Enter How much TranpotationExpenses You Have(In The Form Of Percentage) :"))
            tr_r = tr / 100
            self.transpotation_expences=basic_salary*tr_r
        else:
            self.transpotation_expences=0

        cloths = input("If You Have  Cloths Expenses Press y/Y : ")
        if cloths=="y":
            cl = float(input("Enter How much ClothsExpenses You Have(In The Form Of Percentage) :"))
            cl_r = cl / 100
            self.clothing_expences=basic_salary*cl_r
        else:
            self.clothing_expences=0

        medical=input("If You Have Medical Expenses Press y/Y :")
        if medical=="y":
            me = float(input("Enter How much ClothsExpenses You Have(In The Form Of Percentage) :"))
            me_r = me / 100
            self.medical_expences=basic_salary*me_r
        else:
            self.medical_expences=0

        self.total_expences = self.taxes + self.cell_phone_expences + self.food_expences + self.transpotation_expences + self.clothing_expences + self.medical_expences
        self.savings = basic_salary - self.total_expences


    def display(self):
       print("--------------------------------------------------------")
       print("Your Monthly Income And Expenses")
       print("Your Monthly Salary : ",basic_salary)
       print("Tax Expenses :", self.taxes)
       print("CellPhone Expenses :", self.cell_phone_expences)
       print("Food Expenses :", self.food_expences)
       print("Transpotation Expenses:", self.transpotation_expences)
       print("Clothing Expenses:", self.clothing_expences)
       print("Medical Expenses:", self.medical_expences)
       print("Total Monthly Expenses:", self.total_expences)
       print("After Expenses Your Saving Amount is:", self.savings)
       print("-------------------------------------------------------------")

#calling block
emp=employee()
emp.salary()
emp.display()




