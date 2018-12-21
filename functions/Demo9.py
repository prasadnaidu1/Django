a = 100
def fun1():
    global a
    a = 50
    print(a)

print(a)
fun1()
print(a)