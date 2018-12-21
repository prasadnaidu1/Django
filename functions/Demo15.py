
def display(name,idno=0,salary=0.0):
    print("IDNO = ",idno)
    print("NAME = ",name)
    print("SALARY = ",salary)

# display() # display() missing 1 required positional argument: 'name'
display("Ravi")
display(salary=185000.00,idno=102,name="Kumar")