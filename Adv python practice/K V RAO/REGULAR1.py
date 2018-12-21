
import re
ptr=re.compile("a")
match=ptr.finditer("python is functional object oriented programming language and python is very easy to learn.")
no_of_occurences=0
for m in match:
    no_of_occurences+=1
    print("start: {}   end: {}     group:{}  ".format(m.start(),m.end(),m.group()))
print("no of occurences :",no_of_occurences)
