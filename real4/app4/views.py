from django.shortcuts import render
from firebase import firebase as fab
fa = fab.FirebaseApplication("https://employee-23752.firebaseio.com/infodetails",None)

# Create your views here.
def showindex(request):

    return render(request,"index.html")
def registernew(request):
    id=request.GET.get("update_id")
    if id==None:
        d2 = fa.get("infodetails/", None)
        key = 0
        if d2 == None:
            key = 201
        else:
            for x in d2:
                key = x
            key = int(key) + 1
            return render(request,"register.html",{"key":key})
    else:
        d3=fa.get("infodetails/",id)
        return  render(request,"register.html",{"key":id,"name":d3["name"],"cno":d3["cno"]})
def registerationdetails(request):
    id=request.POST.get("idno")
    name=request.POST.get("name")
    cno=request.POST.get("cno")
    d1={"name":name,"cno":cno}
    fa.put("infodetails/",id,d1)
    return render(request,"register.html",{"msg":"Data Successfully Saved"})
def viewshow(request):
    d2 = fa.get("infodetails/",None)
    return render(request,"views.html",{"emp":d2})
def deldetails(request):
    id=request.POST.get("delete_id")
    fa.delete("infodetails/",id)
    return viewshow(request)