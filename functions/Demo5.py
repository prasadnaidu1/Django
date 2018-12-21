def div(no1,no2):
    return (no1+no2)
def mul(no1,no2):
    print("The sum = ",div(no1,no2))
    return no1-no2
def sub(no1,no2):
    print("The sub = ",mul(no1, no2))
    return no1*no2
def add(no1,no2):
    print("The Mul = ",sub(no1,no2))
    return no1/no2

a = int(input("1st No : "))
b = int(input("2nd No : "))
print("The Div = ",add(a,b))