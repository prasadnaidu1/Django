lst = []
while True:
    name = input("enter name :")
    lst.append(name)
    ans = input("continue press y")
    if ans == "y":
        continue
    else:
        print(lst)
        res = len(lst)
        print(res)
        break
class management:
    def putdetails(self):
        self.type=input("Enter type of items(type veg/nonveg :")
        self.no_of_items=int(input("enter no of items:"))
        if self.type=="veg":
            vegbiryani = int(input("Enter your Veg biryni cost :"))
            vegprice=vegbiryani*self.no_of_items
            split_vegprice=vegprice/res

            if vegprice>=500:
                veg_discount=vegprice*0.05
                total_veg_price=vegprice-veg_discount
                split_vegprice1 = total_veg_price / res
                print("----------------------------------------------")
                print("Your Choosing Item is :",self.type)
                print("Your total payment is :", total_veg_price)
                print("Your discount is :", veg_discount)
                print("Your payble amount is :", total_veg_price-veg_discount)
                print("-------------------------------------------------------")
                print("Indivisual bills :")
                for x in lst:
                    print(x, "---".format(lst), "---", split_vegprice1)
            else:
                print("----------------------------------")
                print("Your Choosing Item is :",self.type)
                print("Your total payment is :",vegprice )
                print("----------------------------------")
                print("Indivisual bills :")
                for x in lst:
                    print(x, "---".format(lst), "---", split_vegprice)
        if self.type=="nonveg":
            nonveg = int(input("Enter your nonVeg biryni cost :"))
            nonveg=nonveg*self.no_of_items
            split_nonveg=nonveg/res

            if nonveg>=1000:
                nonveg1=nonveg*0.05
                total_nonveg_price=nonveg-nonveg1
                split_nonveg1=total_nonveg_price/res
                print("--------------------------------------------------")
                print("Your Choosing Item is :", self.type)
                print("Your total payment is :",total_nonveg_price)
                print("Your discount is :", nonveg1)
                print("Your discount is :", total_nonveg_price-nonveg1)
                print("------------------------------------------------------")

                for x in lst:

                    print("Indivisual bills :")
                    print(x, "---".format(lst), "---", split_nonveg1)

            else:
                print("--------------------------------------")
                print("Your Choosing Item is :",self.type)
                print("Your total payment is :",nonveg )
                print("-----------------------------------")
                print("Indivisual bills :")
                for x in lst:
                    print(x, "---".format(lst), "---", split_nonveg)

        else:
            print("Thanks")








#calling block
m=management()
m.putdetails()



        #amount = int(input("enter amount :"))
        #final = amount / res
        #for x in lst:
          #  print(x, "---".format(lst), "---", final)