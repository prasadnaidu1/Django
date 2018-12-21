x=1000
def function1():
    i=4000
    print("The sum of i+x is",i+x)
class sample:
    comp_name="Sathya Technologies"
    @staticmethod
    def fun1():
        global x
        i=100
        print("The sum of i+x is", i + x)

    def fun2(self,id=0, name=None,sal=0.0):
        self.id=int(input("Enter Employee id : "))
        self.name=input("Enter Name : ")
        self.salary=float(input("Enter employee salary"))
    def dispaly(self):
        print("comapany name : ",sample.comp_name)
        print("Employee id : ",self.id)
        print("Employee name : ",self.name)
        print("Employee Salary : ",self.salary)

