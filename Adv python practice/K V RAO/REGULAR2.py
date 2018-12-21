import re
match=re.finditer("ab","aabaabaabababaab")
no=1
for m in match:
    no+=1
    print("start:{}   end:{}     group:{}  ".format(m.start(),m.end(),m.group()))
print("no of occurences :",no)
