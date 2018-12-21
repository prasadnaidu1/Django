from django.shortcuts import render
from firebase import firebase as fab
def showindex(request):
    return  render(request,"index.html")
def validate(request):
    name = request.POST.get("t1")
    age = request.POST.get("t2")
    cno = request.POST.get("t3")
    d1={"name":name,"age":age}
    fa = fab.FirebaseApplication("https://student-5f369.firebaseio.com/", None)
    fa.put("studentplan",cno,d1)
    return render(request,"index.html",{"emp":d1,"message":"successfully saved"})





