from django.shortcuts import render
from .models import student
from .models import faculity

# Create your views here.
def index(request):
    return  render(request,"index.html")

def head(request):
    return render(request,"head.html")

def menu(request):
    return render(request,"menu.html")

def body(request):
    return render(request,"body.html")

def student_register(request):
    res=student.objects.all()
    print(res)
    return render(request,"student_registration.html",{"ans":res})
def student_registerdetails(request):
    s_id=request.POST.get("id")
    s_uname=request.POST.get("uname")
    s_upass=request.POST.get("upass")
    s_cno=request.POST.get("cno")
    s_email=request.POST.get("email")
    s_course=request.POST.getlist("course")
    s1=student(s_id,s_uname,s_upass,s_cno,s_email,s_course)
    s1.save()
    d1={"status":"datasaved",}
    res=student.objects.all()
    return render(request,"student_registration.html",{"ans":res})


def student_login(request):
    return render(request,"student_login.html")


def student_logindetails(request):
    uname=request.POST.get("uname")
    print(uname)
    upass=request.POST.get("upass")
    print(upass)
    s1= student.objects.filter(username=uname,password=upass)
    print(s1)
    if not s1:
        return render(request,"student_login.html")
    else:
        print("invalid user")
        return render(request,"welcome.html")


def faculity_register(request):
    res=faculity.objects.all()
    return render(request,"faculity_register.html",{"ans":res})


def faculity_registeration(request):
    f_name=request.POST.get("fname")
    print(f_name)
    gender=request.POST.get("gender")
    f_cno=request.POST.get("fcno")
    f_exp=request.POST.get("fexp")
    f_course=request.POST.getlist("t1")
    s2=faculity(f_name,gender,f_cno,f_exp,f_course)
    print(s2)
    s2.save()
    d2={"ans":"datasaved"}
    res = faculity.objects.all()
    return render(request,"faculity_register.html",{"ans":res})