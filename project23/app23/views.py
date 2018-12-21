from django.shortcuts import render
from firebase import firebase as fab
def showindex(request):
    return  render(request,"index.html")
def showdetails(request):
    name = request.POST.get("t1")
    age = request.POST.get("t2")
    cno = request.POST.get("t3")
    d1 = {"name":name,"age":age}
    fr = fab.FirebaseApplication("https://student-5f369.firebaseio.com/",None)
    fs = fr.put("https://student-5f369.firebaseio.com/userdetails",cno,d1)
    f_get = fr.get("https://student-5f369.firebaseio.com/userdetails",None)
    return render (request,"index.html",{"emp":f_get,"message":"successfully saved"})





