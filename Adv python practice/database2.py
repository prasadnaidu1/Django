import sqlite3 as sql
con=sql.connect("product.db")
cur=con.cursor()
while True:
    ans = input("Do Want Insert Records. Press Y/y:")
    if ans=="y" or ans=="Y":
         pno=int(input("Enter Product Number: "))
         pname=input("Enter Product Name: ")
         pprice=float(input("Enter Product Price: "))
         cur.execute("insert into product values(?,?,?)",(pno,pname,pprice))
         print("---------------------------------------------------------------------------")
         print("Pno : {}   Pname : {}  Pprice : {}  Are Inserted ".format(pno,pname,pprice))
         print("----------------------------------------------------------------------------")
         print("Details Saved in Database")
         continue

    else:
        while True:
            res1=input("Do You Want Delete Records. Press Y/y :")
            if res1=="y" or res1=="Y":
                 no=int(input("Enter Record No :"))
                 cur.execute("delete from product where pno=?",(no,))
                 print("-----------------------------------")
                 print("Pno : {}  Are Deleted".format(no))
                 print("-------------------------------------")
                 continue

            else:
                while True:
                    res2=input("Do You Want To Update Records. Press Y/y:")
                    if res2=="y" or res2=="Y":
                        pname = input("Enter Product Name:")
                        pprice = input("Enter Product Price:")
                        pno = input("Enter Product No:")
                        cur.execute("update product set pname=?,pprice=? where pno=?", (pname, pprice, pno))
                        print("--------------------------------------------------------")
                        print("Pname :{} Pprice :{} Are Updated".format(pname,pprice))
                        print("--------------------------------------------------------")
                        ans=input("If You Want To Update Another Record Press y :")
                        if ans=="y":
                            continue
                        else:
                            break

                    else:
                        break
            break


    break

cur.close()
con.commit()
con.close()
