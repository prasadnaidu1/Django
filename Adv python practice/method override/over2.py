class sample:
    def assign(self,id=0,name=None,sal=0.0):
        self.empid=id
        self.empname=name
        self.empsal=sal
    def display(self):
        print(self.empid)
        print(self.empname)
        print(self.empsal)
#calling block
s1=sample()
s1.assign()
s1.display()
print("========")

s2=sample()
s2.assign(id=101,name="prasad")
s2.display()
print("============")
s3=sample()
s3.assign(sal=40000.0 ,id=190)
s3.display()