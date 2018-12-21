from django.shortcuts import render
from firebase import firebase as fab
fa=fab.FirebaseApplication("https://logindetails-d15a1.firebaseio.com/",None)
def showindex(request):
    return render(request,"index.html")


def register(request):
    return render(request,"register.html")


def viewdetails(request):
    e2=fa.get("login/",None)
    return render(request,"views.html",{"res":e2})



def registrationdetails(request):
    name=request.POST.get("name")
    age=request.POST.get("age")
    cno=request.POST.get("cno")
    uname=request.POST.get("uname")
    upass=request.POST.get("upass")
    d1={"name":name,"age":age,"cno":cno,"uname":uname,"upass":upass}
    d2=fa.put("https://logindetails-d15a1.firebaseio.com/","login/",d1)

    return render(request,"register.html",{"msg":"successfully saved"})


def logindetails(request):
    return render(request,"login.html")


def loginsaveddetails(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    d2 = fa.get("login/", None)
    print(d2)
    if d2 ["uname"]==username and d2["upass"]==password:
       return  render(request,"welcome.html")
    else:
       print("invalid user")
       return render(request,"login.html",{"message":"invalid user"})
