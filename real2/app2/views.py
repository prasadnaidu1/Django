from django.shortcuts import render
from firebase import firebase as fa
fb = fa.FirebaseApplication("https://employee-23752.firebaseio.com/details", None)
def showindex(request):
    return render(request,"index.html")
def registerdetails(request):
    id=request.GET.get("update_id")
    if id==None:
        d2=fb.get("details/",None)
        key=0
        if d2==None:
            key=101
        else:
            for x in d2:
                key=x
        key=int(key)+1
        return render(request,"register.html",{"key":key})
    else:
        d1 = fb.get("details/", id)
        return render(request,"register.html",{"key":id,"name":d1["name"],"cno":d1["cno"],"gmail":d1["gmail"]})


def registrationdetails(request):
    idno=request.POST.get("idno")
    name= request.POST.get("name")
    cno=request.POST.get("cno")
    gmail=request.POST.get("gmail")
    d1={"name":name,"cno":cno,"gmail":gmail}
    fr=fb.put("details/",idno,d1)
    return render(request,"register.html",{"message":"successfully saved"})
def viewdetails(request):
    f_get=fb.get("https://employee-23752.firebaseio.com/details/",None)
    return render(request,"views.html",{"emp":f_get,"msg":"getting successfully"})

def deletedetails(request):
    id=request.POST.get("delete")
    fire=fb.delete("details/",id)
    return viewdetails(request)