import re
emailAddress =input("enter email:")
pat2 = "(^\d)"
r2 = re.findall(pat2,emailAddress)
print (r2)
