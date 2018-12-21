lst=[1,2,3,4,55,6,7,8,9]
sq=filter(lambda x:x%2==0,lst)
square=list(map(lambda x:x**2,sq))
print(square)

