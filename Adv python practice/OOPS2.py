#Write a program on class example without creating any object.
class demo:
    comp_name="Prasad Technologies"
    Comp_adds="hyd"
    @staticmethod
    def dispaly(x,y):
        print("Company Name:",demo.comp_name)
        print("Company Adds :",demo.Comp_adds)
        i=x
        j=y
        print("The sum of above values is:",i+j)
#calling block
demo.dispaly(20,40)

