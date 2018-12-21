a = 100
def fun1(i,j):
    print(i+a)
    print(j+a)
def fun2():
    global a
    a = 1000
    print(a)
def fun3():
    global b
    b = 100
    return (a+b)
