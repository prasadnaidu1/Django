while True:
    try:
        units=int(input("enter a number of units:"))
        if units<=150:
            price=2
            res=units*price
            print("your current bill is :",res)
        elif units>=150 or units<=300:
            price1=5.46
            res1=units*price1
            print("your current bill is :", res1)
        elif units>=300:
            price2=6.46
            res2=units*price2
            print("your current bill is :", res2)
        ans=input("do want to repeat press y/Y : ")
        if ans=="y" or ans=="Y":
            continue
        else:
            break
    except ValueError as ve:
        print(ve)

