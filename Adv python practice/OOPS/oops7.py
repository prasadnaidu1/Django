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
s1=sample()
print("Company name :",sample.comp_name)
print("company adds :",sample.comp_adds)
s1.fun1(101,"ravi")
s1.show()
print("======================")
s2=sample()
print("Company name :",sample.comp_name)
print("company adds :",sample.comp_adds)
s2.fun1(103,"prasad")
s2.show()
print("======================")
s3=sample()
print("Company name :",sample.comp_name)
print("company adds :",sample.comp_adds)
s3.fun1(106,"kumar")
s3.show()
print("======================")
s4=sample()
print("Company name :",sample.comp_name)
print("company adds :",sample.comp_adds)
s4.fun1(109,"raju")
s4.show()


