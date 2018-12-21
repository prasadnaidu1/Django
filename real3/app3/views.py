from django.shortcuts import render
from firebase import firebase as fab
fa=fab.FirebaseApplication("https://employee-23752.firebaseio.com/",None)
def showindex(request):
    return render(request,"index.html")
def register_details(request):
    d2 = fa.get("Details/", None)
    key = 0
    if d2 == None:
        key = 101
    else:
        for x in d2:
            key = x
        key = int(key) + 1
    return render(request,"register.html",{"msg":key})
def registratation_details(request):
    idno=request.POST.get("idno")
    name=request.POST.get("name")
    age=request.POST.get("age")
    cno=request.POST.get("cno")
    email = request.POST.get("email")
    dob = request.POST.get("dob")
    adds = request.POST.get("address")
    d1={"name":name,"age":age,"cno":cno,"email":email,"dob":dob,"adds":adds}
    f_get=fa.put("Details/",idno,d1)
    return render(request,"register.html",{"message":"data saved into firebase"})
def viewsdetails(request):
    d2 = fa.get("Details/", None)
    return render(request,"views.html",{"emp":d2})