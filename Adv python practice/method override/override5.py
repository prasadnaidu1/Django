class sample:
    def assign(self):
        self.a=int(input("Enter A value  for Sum : "))
        self.b=int(input("Enter B value  for Sum : "))
        print("==========================================")
        print( "a:{}    b:{}    a+b:{}".format(self.a,self.b,self.a+self.b))
        print("============================================================")
class sample1(sample):
    def assign(self):
        super().assign()
        self.a = int(input("Enter A value for Sub : "))
        self.b = int(input("Enter B value for SUb :"))
        print("=============================================================")
        print("a:{}    b:{}    a-b:{}".format(self.a, self.b, self.a - self.b))
        print("===============================================================")
class sample3(sample1):
    def assign(self):
        super().assign()
        self.a = int(input("Enter A value for Mul : "))
        self.b = int(input("Enter B value for Mul : "))
        print("==============================================================")
        print("a:{}    b:{}    a*b:{}".format(self.a, self.b, self.a * self.b))

#calling block
s1=sample3()
while True:
    s1.assign()
    print("==========================================")
    ans=int(input(" To continue this program press 1: "))
    print("============================================")
    if ans==1:
        continue
    else:
        break
