import csv

from django.http import HttpResponse
from django.shortcuts import render
from .models import account
from .models import deposite
from .models import withdraw

# Create your views here.
def showindex(request):
    return render(request,"Home.html")

def head(request):
    return render(request,"Head.html")

def body(request):
    return render(request,"Body.html")


def accountdetails(request):
    res = account.objects.all()
    return render(request,"Account_View_Details.html",{"msg":res})

def open(request):
    return render(request,"AccountOpen.html")

def accountopen(request):
    name=request.POST.get("t1")
    cno=request.POST.get("t2")
    email=request.POST.get("t4")
    address=request.POST.get("t5")
    a1=account(name,cno,email,address)
    a1.save()
    res = account.objects.all()
    return render(request,"AccountOpen.html",{"msg":"Details Saved"})

def accountcsvfile(request):
    response=HttpResponse(content_type="text/csv")
    response['Content-Disposition']='attachment';filename="accountdetails.csv"
    wr=csv.writer(response)
    res = account.objects.all()
    for x in res:
        wr.writerow([x.name,x.cno,x.email,x.address])
    return response


def manager(request):

    return render(request,"ManagerLogin.html")


def managerdetails(request):
    m_uname=request.POST.get("m1")
    m_upass=request.POST.get("m2")
    if m_uname=="manager" and m_upass=="bank":
        return render(request,"ManagerAll_Details.html")
    else:
        return render(request,"ManagerLogin.html")



def deposite1(request):
    return render(request,"Deposite.html")

def depositedetails(request):
    a_no=request.POST.get("a1")
    a_name=request.POST.get("a2")
    a_money=request.POST.get("a3")
    a_date=request.POST.get("a5")
    a_type=request.POST.get("a4")
    acc=deposite(D_no=a_no,D_name=a_name,D_money=a_money,A_date=a_date,A_type=a_type)
    acc.save()
    return render(request,"Deposite.html",{"message":"Amount Deposited"})


def depo(request):
    ans=deposite.objects.all()
    return render(request,"Deposite_View_Details.html",{"msg1":ans})

def depositeCSVfile(request):
    http=HttpResponse(content_type="text/csv")
    http['Content-Disposition']='attachment';filename="deposite.csv"
    w=csv.writer(http)
    res2=deposite.objects.all()
    for x in res2:
        w.writerow([x.D_no,x.D_name,x.A_money,x.A_date,x.A_type])
    return http


def withdraw(request):
    return render(request,"Withdraw_View_Details.html")

def withdrawlogin(request):
    return render(request,"Withdraw.html")
def withdrawlogindetails(request):
    a_no = request.POST.get("a1")
    a_name = request.POST.get("a2")
    dep2 = deposite.objects.filter(D_no=a_no, D_name=a_name)
    if dep2:
        dep3=deposite.objects.values_list()
        return render(request,"Withdraw_View_Details.html",{"ans1":dep3})
    else:
        return render(request,"Withdraw.html")

    #dep1=deposite.objects.filter(D_no=a_no,D_name=a_name)
    #if not dep1:
     #   return  render(request,"Withdraw.html")
    #else:
     #   return render(request, "Withdraw_View_Details.html")


def withdrawdetails(request):
    w_money=request.POST.get("y1")
    print(w_money)
    #dep=deposite.objects.filter(D_money=w_money)
    #print(dep)  
    w_date=request.POST.get("y2")
    w_type=request.POST.get("y3")
    from firebase import firebase as fab
    fa=fab.FirebaseApplication("https://djangoweb1-ec1db.firebaseio.com/",None)
    fa.put("https://djangoweb1-ec1db.firebaseio.com/","withdraw/",None)
    return render(request,"Withdraw_View_Details.html")