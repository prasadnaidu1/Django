class Circle:
    def  area(self):
        self.r=float(input("Enter radious for area : "))
        self.rc=3.147*self.r*self.r
        print("area of circle is :" ,self.rc)
    def peri(self):
        self.r = float(input("Enter radious for peri : "))
        self.pa=2*3.147*self.r
        print("area of peri circle :", self.pa)
class Rect(Circle):
        def area(self):
            super().area()
            self.l = float(input("Enter length : "))
            self.b = float(input("Enter breadth : "))
            self.rc1 = self.l * self.b
            print("area of rect is :", self.rc1)
        def peri(self):
            super().peri()
            self.l = float(input("Enter  peri length : "))
            self.b = float(input("Enter  peri breadth : "))
            self.pa = 2*(self.l*self.b)
            print("area of peri rect :", self.pa)
class Squre(Rect):
        def area(self):

                super().area()
                self.s = float(input("Enter side value : "))
                self.sa = self.s * self.s
                print("area of squre is :", self.sa)



        def peri(self):
            super().peri()
            self.s = float(input("Enter  peri side value : "))
            self.ps = 4 * self.s
            print("area of pe  ri of squre :", self.ps)



#calling block
s=Squre()
while True:
    s.area()
    print("======================================")
    s.peri()
    ans= input("to continue the program to presss y :")
    if ans=="y":
        continue
    else:break

