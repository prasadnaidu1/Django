from django.shortcuts import render
from firebase import firebase as fab

def showindex(request):
    fa=fab.FirebaseApplication("https://loginpage-9f66f.firebaseio.com/login",None)
    d1=fa.get("login/", None)
    return render(request,"firebase.html",{"emp":d1})

