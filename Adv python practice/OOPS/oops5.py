class sample:
    comp_name=input("enter your company name :")
    comp_adds=input("enter your company adds : ")
    def fun1(self ,id, name):
        self.id=id
        self.name=name

    def show(self):
        print("Employee id :",self.id)
        print("Employee name :",self.name)
#calling block
a=int(input("enter employee id  number :"))
b=input("enter employee name : ")
s1=sample()
s1.fun1(a,b)
print("company name :",sample.comp_name)
print("company adds :",sample.comp_adds)
s1.show()
print("========================================")