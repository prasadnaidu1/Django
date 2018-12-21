class sample:
    def demo(self,*args):
        res=0
        for x in args:
            res+=x

        print(res)
#calling block
s1=sample()
s1.demo()
s1.demo(1,2)
s1.demo(1,2,3,4)