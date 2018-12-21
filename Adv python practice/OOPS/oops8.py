class sample:
    comp_name=input("Enter company name :")
    comp_adds=input("Enter company address :")
    @staticmethod
    def assign( id ,name):
        employee_id=id
        employee_name=name
        print(id)
        print(name)
#calling block
x=int(input("eneter a number : "))
y=input("enter a name : ")
s1=sample()
print(sample.comp_name)
print(sample.comp_adds)
s1.assign(x,y)





