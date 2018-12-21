from django.shortcuts import render
from firebase import firebase as fab
fa=fab.FirebaseApplication("https://student-5f369.firebaseio.com/",None)

def showindex(request):
    return render(request,"index.html")
def register(request):
    id=request.GET.get("update_id")
    fa = fab.FirebaseApplication("https://student-5f369.firebaseio.com/Employee", None)
    if id==None:
        fire2 = fa.get("Employee/", None)
        key = 0
        if fire2 == None:
            key = 201
        else:
            for x in fire2:
                key = x
        key = int(key) + 1
        return render(request,"register.html",{"key":key} )
    else:
        fa = fab.FirebaseApplication("https://student-5f369.firebaseio.com/Employee", None)
        d2=fa.get("Employee/",id)
        return render(request,"register.html",{"key":id,"name":d2["name"],"cno":d2["cno"]})

def registratation(request):
    idno=request.POST.get("idno")
    name=request.POST.get("name")
    cno=request.POST.get("cno")
    d1={"name":name,"cno":cno}
    fa.put("Employee/",idno,d1)
    return render(request,"register.html",{"message":"successfully saved data"})

def viewdetails(request):
    fire = fab.FirebaseApplication("https://student-5f369.firebaseio.com/Employee", None)
    f_get = fire.get("https://student-5f369.firebaseio.com/Employee/", None)
    return render(request,"viewdetails.html",{"emp":f_get})

def deletedetails(request):
    id=request.POST.get("delete_id")
    fire = fab.FirebaseApplication("https://student-5f369.firebaseio.com/Employee", None)
    f_get = fire.delete("Employee/",id)
    return viewdetails(request)