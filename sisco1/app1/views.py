from django.shortcuts import render
from.models import friends

# Create your views here.
def showindex(request):
    id=request.GET.get("update_id")
    if id==None:
        res=friends.objects.all()
        return render(request,"index.html",{"res":res})
    else:
        id1=friends.objects.filter(entry=id).update()
        print(id1)
        return render(request,"index.html",{"id":id})

def displaydetails(request):
    entry= request.POST.get("eno")
    date= request.POST.get("date")
    amount= request.POST.get("amt")
    members= request.POST.getlist("t1")
    i=(", ".join(members))
    t=len(members)
    t1=int(amount)/t
    fr=friends(entry,date,amount,i,t1)
    fr.save()
    res=friends.objects.all()
    d1={"msg":"datasaved"}
    return render(request,"index.html",{"res":res})


def deletedetails(request):
    id=request.POST.get("delete_id")
    friends.objects.filter(entry=id).delete()
    res=friends.objects.all()
    return render(request,"index.html",{"res":res})