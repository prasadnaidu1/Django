#EMAIL VALIDATION
import re
email=input("enter your email id :")
exp=re.search("[^@]+@[^@]+\.[^@]+",email)
if exp:
    print("valid")
else:
    print("invalid")
