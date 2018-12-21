d1={"name":"prasad","id":101,"sal":128000.00}
for x in d1:
    print(x)
print("--------------------")
for x in d1:
    print(x,"--",d1[x])
print("---------------------")
for x in d1:
    print(d1[x])
print("------------------")
for x,y in d1.items():
    print(x,"--",y)
print("------------ ----------")
d1={101:[89,90,92,89,95]}
d2={102:[89,67,78,90,100]}
for x,y in d1.items():
    print(sum(y))
    print(max(y))
    print(min(y))
print("------d1 over==================")
for x,y in d2.items():
    print(sum(y))
    print(max(y))
    print(min(y  ))
