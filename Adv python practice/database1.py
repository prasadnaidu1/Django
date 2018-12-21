import sqlite3 as sql
con=sql.connect("product.db")
cur=con.cursor()
qry="create table if not exists product(pno number,pname text,pprice real)"
cur.execute(qry)
print("table created")
cur.close()
con.close()