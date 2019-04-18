n=int(input("enter a number"))
num=1
for x in range(0,n):
    for y in range(0,n):
        num=1
        print(end=" ")
    for z in range(0,x+1):
        print(n,end=" ")

        n=n+1
        print()