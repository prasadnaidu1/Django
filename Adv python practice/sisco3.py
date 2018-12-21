lst = []
while True:
    name = input("Enter Name : ")
    lst.append(name)
    ans = input("Continue press y : ")
    if ans == "y":
        continue
    else:
        print(lst)
        res = len(lst)
        print(res)
        break
class management:
    def putdetails(self):
        self.type=input("Enter Type Of Items(Type Veg/Nonveg/Both :")
        if self.type=="veg":
            self.no_of_items = int(input("Enter No Of Vegitems:"))
            vegbiryani = int(input("Enter your Veg biryni cost :"))
            vegprice=vegbiryani*self.no_of_items
            split_vegprice=vegprice/res

            if vegprice>=500:
                veg_discount=vegprice*0.05
                total_veg_price=vegprice-veg_discount
                split_vegprice1 = total_veg_price / res
                print("----------------------------------------------")
                print("Your Choosing Item is :",self.type)
                print("Your Total Payment is :", total_veg_price)
                print("Your Discount is :", veg_discount)
                print("Your payble amount is :", total_veg_price-veg_discount)
                print("-------------------------------------------------------")
                print("Indivisual bills :")
                for x in lst:
                    print(x, "---".format(lst), "---", split_vegprice1)
            else:
                print("----------------------------------")
                print("Your Choosing Item is :",self.type)
                print("Your Total Payment is :",vegprice )
                print("----------------------------------")
                print("Indivisual bills :")
                for x in lst:
                    print(x, "---".format(lst), "---", split_vegprice)
        if self.type=="nonveg":
            self.no_of_items=int(input("Enter No Of NonVegitems:"))
            nonvegcost = int(input("Enter NonVeg biryni cost :"))
            nonveg=nonvegcost*self.no_of_items
            split_nonveg=nonveg/res

            if nonveg>=1000:
                nonveg1=nonveg*0.05
                total_nonveg_price=nonveg-nonveg1
                split_nonveg1=total_nonveg_price/res
                print("--------------------------------------------------")
                print("Your Choosing Item is :", self.type)
                print("Your Total Payment is :",total_nonveg_price)
                print("Your Discount is :", nonveg1)
                print("Your Total Amount :", total_nonveg_price-nonveg1)
                print("------------------------------------------------------")

                for x in lst:

                    print("Indivisual Bills :")
                    print(x, "---".format(lst), "---", split_nonveg1)

            else:
                print("--------------------------------------")
                print("Your Choosing Item is :",self.type)
                print("Your Total Payment is :",nonveg )
                print("-----------------------------------")
                print("Indivisual Bills :")
                for x in lst:
                    print(x, "---".format(lst), "---", split_nonveg)
        if self.type=="both":
            self.no_of_vegitems=int(input("Enter No Of VegItems:"))
            vegbiryani = int(input("Enter your Veg  cost :"))
            vegprice = vegbiryani * self.no_of_vegitems
            self.no_of_nonvegitems = int(input("Enter No Of NonVegItems:"))
            nonvegcost = int(input("Enter  NonVeg  Cost :"))
            nonveg=nonvegcost*self.no_of_nonvegitems
            total_bill=vegprice+nonveg
            split_totalbill=total_bill/res
            if total_bill>2000:
                discount=total_bill*0.10
                total_cost=total_bill-discount
                split_totalcost=total_cost/res
                print("----------------------------")
                print("No of Veg Items : ",self.no_of_vegitems)
                print("Total Veg Amount is : ",vegprice)
                print("--------------------------------------")
                print("No Of NonVeg Items : ",self.no_of_nonvegitems)
                print("Total Veg Amount is : ", nonveg)
                print("-------------------------------------------")
                print("Your Total Bill Without Discount : ",total_bill)
                print("Your Discount is :",discount)
                print("Your Total Bill After Discount(Veg+NonVeg) is :",total_cost)
                print("----------------------------------------------")
                for x in lst:
                    print(x, "---".format(lst), "---",split_totalcost )

            else:
                print("----------------------------")
                print("No of Veg Items : ", self.no_of_vegitems)
                print("Total Veg Amount is : ", vegprice)
                print("--------------------------------------")
                print("No of Nonveg Items : ", self.no_of_nonvegitems)
                print("Total NonVeg Amount is : ", nonveg)
                print("-------------------------------------------")
                print("Your Total Bill Without Discount : ", total_bill)
                print("------------------------------------------------")
                for x in lst:
                    print(x, "---".format(lst), "---",split_totalbill )

        else:
            print("Thanks")

#calling block
#m=management()
#m.putdetails()



