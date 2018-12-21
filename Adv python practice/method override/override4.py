class sample:
    def assign(self):
        self.a=int(input("Enter  A value :"))
        self.b=int(input("Enter  B value :"))
        print(" a={}  b={} a+b={}".format( self.a,self.b,self.a+self.b))
class sample1(sample):
    def assign(self):
        super().assign()
        print(" a={}  b={} a-b={}".format(self.a, self.b, self.a - self.b))
class sample3(sample1):
    def assign(self):
        super().assign()
        print(" a={}  b={} a*b={}".format(self.a, self.b, self.a * self.b))

#calling block
s1=sample3()
while True:
    s1.assign()
    ans=input("To continue to press y :")
    if ans=="y":
        continue
    else:
        break
