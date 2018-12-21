class numbers(object):
    def set(self):
        self.a=10
        self.b=12
        self.a,self.b=self.b,self.a
        print(self.a,self.b)
        print(self.b,self.a)
class strings(numbers):
    def put(self):
        super().set()
        self.s1="prasad"
        self.s2="naidu"
        self.s1,self.s2=self.s2,self.s1
        print(self.s1,self.s2)
        print(self.s2,self.s1)
s=strings()
s.put()