class numbers(object):
    def __init__(self):
        print("i am base class constructor")
    def integers(self):
        self.a=int(input("enter a value : "))
        self.b=int(input("enter b value : "))
        self.a,self.b=self.b,self.a
        print("For swaping integers of a, b : ",self.a,self.b)
        print("For swaping integers of b, a : ",self.b,self.a)
class strings(numbers):

        def __init__(self):
            super().__init__()
            print("i am derived class constructor")
        def put (self):
            while True:
                super().integers()
                self.s1=input("enter first string : ")
                self.s2=input("enter  second string : ")
                self.s1,self.s2=self.s2,self.s1
                print("For swaping strings of s1, s2 : ",self.s1,self.s2)
                print("For swaping strings of s2, s1 : ",self.s2,self.s1)
                ans = input("to continue press y:")
                if ans == 'y':
                     continue
                else:
                    break


#calling block
s=strings()
s.put()

