from django.http import HttpResponse
from django.shortcuts import render
from .models import employee

# Create your views here.

def showindex(request):
    return render(request,"index.html")


def registerdetails(request):
    name=request.POST.get("t1")
    cno=request.POST.get("t2")
    desig=request.POST.get("t3")
    salary=request.POST.get("t4")
    e1=employee(name,cno,desig,salary)
    e1.save()
    return render(request,"index.html",{"msg":"Data Saved In Database"})


def csvfile(request):
    response=HttpResponse(content_type="text/csv")
    response['Content-Disposition']='attachment';filename="employee.csv"
    import csv
    wr=csv.writer(response)

    res=employee.objects.all()
    for x in res:
        wr.writerow([x.name,x.cno,x.desig,x.salary])
    return response