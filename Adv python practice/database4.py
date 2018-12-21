import sqlite3 as sql
con=sql.connect("product.db")
cur=con.cursor()
while True:
    ans = input("do want insert one more record press Y/y:")
    if ans=="y" or ans=="Y":
         pno=int(input("enter product number: "))
         pname=input("enter product name: ")
         pprice=float(input("enter product price: "))
         cur.execute("insert into product values(?,?,?)",(pno,pname,pprice))
         print("Your product no : ",pno)
         print("Your product name : ",pname)
         print("Your product price : ",pprice)
         print("Details Saved in Database")

    res1 = input("Do you want Delete a row press Y/y :")
    if res1 == "y" or res1 == "Y":
        no = int(input("enter deleted row no:"))
        cur.execute("delete from product where pno=?", (no,))
        print(no, "deleted")
    res2 = input("Do you want to Update Your Record Press Y/y:")
    if res2 == "y" or res2 == "Y":
        pname = input("enter product name:")
        pprice = float(input("enter product price:"))
        pno = int(input("enter product no:"))
        cur.execute("update product set pname=?,pprice=? where pno=?", (pname, pprice, pno))
        print("data updated")
        break

    else:
        break
cur.close()
con.commit()
con.close()