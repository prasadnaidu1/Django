#mobile validation
import re
while True:
    try:
        no=input("enter mobile number :")
        if len(no)==10:
            exp=re.match("[6789]+\d+",no)
            if exp:
                print("valid number")
                break
            else:
                print("invalid numebr")
                ans=input(" Do you want to enter another number press y :")
                if ans=="y":
                    continue
                else:
                    break

        else:
            print("you are not entered 10 digits")
            ans1=input("Do you want to enter one more time press y:")
            if ans1=="y":
                continue
            else:
                break
    except:
        print("Enter digits only")
    finally:
        print("Thanks")

