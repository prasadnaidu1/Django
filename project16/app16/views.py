from django.shortcuts import render
from firebase import firebase as fab
def showIndex(request):
    return render(request,"index.html")
def display(request):
    name=request.POST.get("t1")
    age=request.POST.get("t2")
    cno=request.POST.get("t3")
    email=request.POST.get("t4")
    sal=request.POST.get("t5")
    adds=request.POST.get("t6")
    d1={"name":name,"age":age,"contactno":cno,"email":email,"sal":sal,"add":adds}
    fa=fab.FirebaseApplication("https://project-22b00.firebaseio.com/userdata/userdetails/")
    fa.put("https://project-22b00.firebaseio.com/userdata/userdetails","userdetails2",d1)
    return render(request,"details.html",{"msg":"successfully saved"})


