import pickle
from list import student
f=open("satya.db","rb")
print("----------------------")
while True:
    try:
        s=pickle.load(f)
        s.studentdetails()
        s.display()
    except:
        print("-------------------------------")
        f.close()
        break
