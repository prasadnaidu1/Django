from firebase import firebase as fab
fa = fab.FirebaseApplication("https://student-5f369.firebaseio.com",None)
d1 = fa.get("https://student-5f369.firebaseio.com/details",None)
for a,b in d1.items():
    print(a,"....",b)

print("thanks")
