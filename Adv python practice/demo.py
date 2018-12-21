from list import student
import pickle
f=open("satya.db","wb")
rows=int(input("enter rows how many rows you want : "))
for i in range(rows):
    print("----------------------------------")
    print("enter "+str(i+1)+"student details")
    print("-----------------------------------")
    id=int(input("enter student number : "))
    name=input("enter student number :")
    s=student()
    s.studentdetails(id,name)
    pickle.dump(s,f)
    print(i+1,"student details saved")
    print("-----------------------")
    s.dispaly()
print("successfully complete")
f.close()
