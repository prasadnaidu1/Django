



lst=[]
while True:
    name=input("enter name :")
    lst.append(name)
    ans=input("continue press y")
    if ans=="y":
        continue
    else:
        print(lst)
        res=len(lst)
        print(res)
        break
amount=int(input("enter amount :"))
final=amount/res
for x in lst:
    print(x,"---".format(lst),"---",final)



