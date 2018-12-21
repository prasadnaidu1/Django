class sample:
    def fun1(self):
        self.empid=int(input("enter a employee id: "))
        self.empname=input("enter a employee name : ")
        self.empsal=float(input("enter a employee sal : "))
    def display(self):
        print("employee id :" ,self.empid)
        print("employee name :" ,self.empname)
        print("employee sal :" ,self.empsal)
class sample2(sample):
    def fun2(self):
        super().fun1()
        self.emp_dailyallowences=self.empsal*0.10
        self.emp_travelling_allownces=self.empsal*0.05
        self.total_travelling_allowences=self.empsal+self.emp_travelling_allownces
        self.total_salary=self.empsal+self.emp_dailyallowences+self.total_travelling_allowences

    def show(self):
        super().display()
        print("employee daily allowences : ",self.emp_dailyallowences)
        print("employee travelling allowences : ",self.emp_travelling_allownces)
        print("employee total_travelling allowences : ",self.total_travelling_allowences)
        print("employee total_salary : ",self.total_salary)


#calling block
s1=sample2()
s1.fun2()
s1.show()

