l1=[1,22,2,4,2,4,6,43,43,2,2,4]
l2=list(set(l1))#for converting list to set
print(l2)
l2.sort(key=l1.index)#for same index positions
print(l2)
l2.sort(reverse=True)#for decnding order
print(l2)
l2.sort()#for assending order
print(l2)