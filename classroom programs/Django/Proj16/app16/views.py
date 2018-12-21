from django.shortcuts import render

def showIndex(request):
    from .models import Product
    res = Product.objects.all()
    return render(request,"index.html",{"pro":res})


def register(request):
    pno = int(request.POST.get("pno"))
    pname = request.POST.get("pname")
    pprice = float(request.POST.get("pprice"))
    pqty = int(request.POST.get("pqty"))

    print(pno,pprice,pname,pqty )
    #from app16.models import Product
    from .models import Product
    p1 = Product(no=pno,qty=pqty,price=pprice,name=pname)
    p1.save()

    d1 = {"message":"Product Saved"}
    res = Product.objects.all()
    return render(request, "index.html", {"pro": res})


def delete(request):
    del_no = int(request.POST.get("delete_id"))
    from .models import Product
    Product.objects.filter(no=del_no).delete()
    res = Product.objects.all()
    return render(request, "index.html", {"pro": res})
