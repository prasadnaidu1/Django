class sample:
    def assign(self,a,b):
        self.a=a
        self.b=b
        print( self.a+self.b)
class sample1(sample):
    def assign(self,a,b):
        super().assign(a,b)
        self.a=a
        self.b=b
        print(self.a-self.b)
class sample3(sample1):
    def assign(self,a,b):
        super().assign(a,b)
        self.a=a
        self.b=b
        print(self.a*self.b)

#calling block
s1=sample3()
s1.assign(12,34)
