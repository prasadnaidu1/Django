import csv

from django.http import HttpResponse
from django.shortcuts import render
from .models import courses
from.models import faculity
from .models import student
from app2.functions.functions import *
from firebase import firebase as fab
fa=fab.FirebaseApplication("https://studentdetails2-6d1de.firebaseio.com/",None)

def head(request):
    return render(request,"head.html")
def menu(request):
    return render(request,"menu.html")

def showindex(request):
    return render(request,"display.html")

def admin_login(request):
    return render(request,"admin_login.html")
def admin_login_details(request):
    u_name=request.POST.get("uid")
    u_pass=request.POST.get("upass")
    if u_name=="admin" and u_pass=="admin":
        return render(request,"admin_home.html",{"message":"Successfully Logined"})
    else:
        return render(request,"admin_login.html")
def course(request):
    res=courses.objects.all()
    return render(request, "view_courses.html", {"msg":res})


def addcourse(request):
    return render(request,"add_course.html")

def addcoursedetails(request):
    c_name=request.POST.get("cname")
    c_id=request.POST.get("cid")
    c_fee=request.POST.get("cfee")
    c_duration=request.POST.get("cdur")
    c1=courses(CourseName=c_name,CourseId=c_id,CourseFee=c_fee,CourseDuration=c_duration)
    c1.save()
    res = courses.objects.all()
    return render(request,"add_course.html",{"res":"Registered Your Course successfully"})

def coursedelete(request):
    id=request.POST.get("delete_id")
    print(id)
    courses.objects.filter(CourseId=id).delete()
    courses.objects.all()
    return course(request)

def courseupdate(request):
    id = request.GET.get("update_id")
    print(id)
    courses.objects.filter(CourseId=id).update()
    return render(request,"add_course.html",{"id":id})


def cousecsvfile(request):
    response=HttpResponse(content_type="text/csv")
    response['Content-Dispostion']='attachment';filename="course.csv"
    wr=csv.writer(response)
    c1=courses.objects.all()
    for x in c1:
        wr.writerow([x.CourseName,x.CourseId,x.CourseFee,x.CourseDuration])
    return response

def faculity1(request):
    ans = faculity.objects.all()
    return render(request, "view_faculity.html", {"res1": ans})


def addfaculity(request):
    return render (request,"add_faculity.html")

def addfaculitydetails(request):
    f_id=request.POST.get("t1")
    f_name=request.POST.get("t2")
    f_gender=request.POST.get("t5")
    f_cno=request.POST.get("t6")
    f_course=request.POST.get("t3")
    f_exp=request.POST.get("t4")
    f1=faculity(id=f_id,name=f_name,gender=f_gender,cno=f_cno,course=f_course,exp=f_exp)
    f1.save()
    ans = faculity.objects.all()
    return render(request,"add_faculity.html",{"status":"Faculity Added"})

def faculitycsvfile(request):
    response1 = HttpResponse(content_type="text/csv")
    response1['Content-Dispostion'] = 'attachment';filename="faculity.csv"
    wr = csv.writer(response1)
    c2 = faculity.objects.all()
    for x in c2:
        wr.writerow([x.id,x.name,x.gender,x.cno,x.course,x.exp])
    return response1

def faculitydelete(request):
    id=request.POST.get("delete_id")
    faculity.objects.filter(id=id).delete()
    faculity.objects.all()
    return faculity1(request)


def faculityupdate(request):
    id=request.GET.get("update_id")
    faculity.objects.filter(id=id).update()
    return render(request,"add_faculity.html",{"id":id})


def student1(request):
    res2=student.objects.all()
    return render(request,"view_student_details.html",{"res2":res2})

def viewstudent(request):
    return render(request,"student_register.html")

def studentdetails(request):
    s_name=request.POST.get("s1")
    s_cno=request.POST.get("s2")
    s_gender=request.POST.get("s6")
    s_uname=request.POST.get("s3")
    s_upass=request.POST.get("s4")
    s_email=request.POST.get("s5")
    s2=student(s_name,s_cno,s_gender,s_uname,s_upass,s_email)
    s2.save()
    s_res = student.objects.all()
    return render(request,"student_register.html",{"status1":"Student Details Added"})


def studentlogin(request):
    return render(request,"student_login.html")

def studentlogindetails(request):
    s_username= request.POST.get("u1")
    s_password=request.POST.get("u2")
    login=student.objects.filter(username=s_username,password=s_password)
    if not login:
        return render(request,"student_login.html")
    else:
        return render(request, "student_welcome_page.html")


def studentwelcomedetails(request):
    sd1=request.POST.get("a1")
    sd2=request.POST.get("a2")
    sd3=request.POST.get("a3")
    sd4=request.POST.get("a4")
    sd5=request.POST.get("a5")
    d1={"name":sd1,"qualification":sd3,"course":sd4,"timings":sd5}
    fa.put("Details",sd2,d1)
    return render(request,"student_welcome_page.html",{"status3":"Details saved in Firebase"})

def studentdelete(request):
   id= request.POST.get("delete_id")
   print(id)
   u1=student.objects.filter(cno=id).delete()
   res=student.objects.all()
   return student1(request)


def studentupdate(request):
    id=request.GET.get("update_id")
    u2=student.objects.filter(cno=id).update()
    return render(request,"student_register.html",{"cno":id})


def studentcsvfile(request):
    response2 = HttpResponse(content_type="text/csv")
    response2['Content-Dispostion'] = 'attachment';filename = "student.csv"
    wr = csv.writer(response2)
    c3 = student.objects.all()
    for x in c3:
        wr.writerow([x.name,x.cno,x.gender,x.username,x.password,x.email])
    return response2


#def faculityimage(request):
 #   if request.method=="POST":
  #      faculity=faculityimage(request.POST)
   #     if faculity.is_valid():
    #        file_upload(request.FILES['file'])
     #       return HttpResponse("fileuploded")
    #else:
     #   faculity=faculityimage(request)
      #  return render(request,"view_faculity.html",{"form":faculity})
