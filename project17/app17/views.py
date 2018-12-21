from django.shortcuts import render
from firebase import firebase as fab

def showIndex(request):
    return render(request,"index.html")
def displayIndex(request):
    name=request.POST.get("t1")
    age=request.POST.get("t2")
    cno=request.POST.get("t3")
    email=request.POST.get("t4")
    salary=request.POST.get("t5")
    adds=request.POST.get("t6")
    d1={"name":name,
        "age":age,
        "cno":cno,
        "email":email,
        "salary":salary,
        "adds":adds}
    fa=fab.FirebaseApplication("https://project-22b00.firebaseio.com/")
    fa.put("https://project-22b00.firebaseio.com/","userdetails",d1)
    return render(request,"details.html",{"message":"successfuly saved"})

