str=input("enter string:")
s={"LETTER":0,"DIGITS":0}
for x in str:
    if x.isdigit():
        s["DIGITS"]+=1
    elif x.isalpha():
        s["LETTER"]+=1
    else:
        pass

print("letters:",s["LETTER"])
print("digits:",s["DIGITS"])