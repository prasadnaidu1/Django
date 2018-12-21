lst=["a","e","i","o","u","A","E","I","O","U"]
while True:
    ch=input("enter a one character:")
    if ch in lst:
        print("given input is vowel")
        print("your input is:",ch)
    else:
        print("given input is consonent")
        print("your input is :",ch)
    ans=input("do you want to run one more time press y/Y:")
    if ans=="y" or ans=="Y":
        continue
    else:
        break
