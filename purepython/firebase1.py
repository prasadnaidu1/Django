
from django.shortcuts import render
from firebase import firebase as fab
fa = fab.FirebaseApplication("https://employee-23752.firebaseio.com/employeedetails/",None)
d1 = fa.get("",None)
for a,b in d1.items():
    print(a)
    for c,d in b.items():
        print(c)
        for e,f in d.items():
            print(e)
            for g,h in f.items():
                print(g)
                for i,j in h.items():
                    print(i,"---",j)

                    print()
print("data saved")


