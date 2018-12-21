class sample:
    college_name="Dr.Agarala Eswar Reddi MBA College"
    college_adds="C.Ramapuram"
    def function1(self):
        self.student_id=int(input("enter id number: "))
        self.student_name=input("enter name :")
        self.student_contactnumber=input("enter contact number: ")
        self.student_address=input("enter address : ")
    def show(self):
        print("College Name :",sample.college_name)
        print("College adds : ",sample.college_adds)
        print("Student Id :",self.student_id)
        print("Student Name :",self.student_name)
        print("Student contactnumber :",self.student_contactnumber)
        print("Student Adderess :",self.student_address)
#calling block
s1=sample()
s1.function1()
s1.show()
print("=================")
print(sample.college_name)
print(sample.college_adds)

print("==============================")