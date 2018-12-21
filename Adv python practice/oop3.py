class sample:
    def fun1(self):
        self.id=int(input("enter a number :"))
        self.name=input("enter name:")
        self.sal=float(input("enter salary:"))
    def dispaly(self):
        print("Employee Id:",self.id)
        print("Employee Name :",self.name)
        print("employee salary:",self.sal)
#calling block
s1=sample()
s1.fun1()
s1.dispaly()