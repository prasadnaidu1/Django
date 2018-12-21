tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
print(li)
for x in tp:
    if tp[x]%2==0:
        li.append(tp[x])
tp2=tuple(li)
print(tp2)