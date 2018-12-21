from django.shortcuts import render

# Create your views here.
def showindex(request):
    from .models import product
    res=product.objects.all()
    return render( request,"index.html",{"res":res})
def register(request):
    pno=int(request.POST.get("no"))
    pname=request.POST.get("name")
    pprice=float(request.POST.get("price"))
    pquantity=int(request.POST.get("qty"))
    #from app5.models import product
    from .models import product
    p1=product(no=pno,name=pname,price=pprice,qty=pquantity)
    p1.save()
    res = product.objects.all()
    return render(request,"index.html",{"message":"data inserted","res":res})

def deletedetails(request):
    del_id=request.POST.get("delete_id")
    from .models import product
    product.objects.filter(no=del_id).delete()
    res = product.objects.all()
    return render(request,"index.html",{"res":res})
def updatedetails(request):
    id=int(request.GET.get("update_id"))
    print(id)
    from .models import product
    u2=product.objects.filter(no=id).update()
    print(u2)
    res = product.objects.all()
    return render(request,"index.html",{"no":id})