from django.shortcuts import render
from .models import employee

# Create your views here.
def showindex(request):
    emp = employee.objects.all()
    return render(request, "index.html",{"pro":emp})
def display(request):
    from .models import employee
    emp = employee.objects.all()
    Eid=int(request.POST.get("id"))
    Ename=request.POST.get("name")
    Ecno=int(request.POST.get("cno"))
    Esal=float(request.POST.get("sal"))
    from app7.models import employee
    e1=employee(Eid,Ename,Ecno,Esal)
    e1.save()
    emp = employee.objects.all()
    return render(request,"index.html",{"pro":emp})

def deletedetails(request):
    del_id=int(request.POST.get("delete_id"))
    print(del_id)
    from .models import employee
    employee.objects.filter(id=del_id).delete()
    emp = employee.objects.all()
    return  render(request,"index.html",{"pro":emp})

def updatedetails(request):
   id = int(request.GET.get("update_id"))
   e2 = employee.objects.filter(id=id).update()
   print(id)
   print(e2)
   e3=employee.objects.filter(id=id).values()
   print(e3)
   return render(request,"index.html",{"no":id})