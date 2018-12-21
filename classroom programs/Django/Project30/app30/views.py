from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showindex(naveen):
    return render(naveen,"index.html")

def saveName(request):
    name = request.POST.get("t1")
    res = HttpResponse("OK")
    res.set_cookie("username",name)
    return res

def showName(request):
    name = request.COOKIES["username"]
    return HttpResponse(name)