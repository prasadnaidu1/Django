from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,"index.html")

def head(request):
    return  render(request,"head.html")

def menu(request):
    return render(request,"menu.html")

def body(request):
    return render(request,"body.html")


def course(request):
    return render(request,"course.html")


def student_login(request):
    S_id=request.POST.get("sid")
    S_pass=request.POST.get("spass")
    if id==S_id and

    return