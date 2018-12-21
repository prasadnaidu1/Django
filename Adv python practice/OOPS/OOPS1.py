#	Write the program on class Example by using static method
class sample:
    com_name="Sathya Technologies"
    @staticmethod
    def assign(id=0,name=None,sal=0.0):
        print("Company Name: " ,sample.com_name)
        print("ID:" ,id)
        print("Name :",name)
        print("sal :" ,sal)

#calling block
s1=sample()
s1.assign()
print("------------------------------")
s2=sample()
s2.assign(id=102)
print("=========================================")
s3=sample()
s3.assign(id=101,name="prasad",sal=40000)
print("=================================================")

