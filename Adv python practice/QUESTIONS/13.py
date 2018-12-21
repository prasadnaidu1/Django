str=input("enter data:")
s={"uppercase":0,"lowercase":0}
for x in str:
    if x.isupper():
        s["uppercase"]+=1
    elif x.islower():
        s["lowercase"]+=1
    else:
        pass
print(s["uppercase"])
print(s["lowercase"])