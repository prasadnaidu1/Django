class circle:
    def square(self,r):
        self.radious=r

    def area(self):
        self.area=self.radious*2*3.14
        print(self.area)
#calling clock
c=circle()
c.square(20)
c.area()
