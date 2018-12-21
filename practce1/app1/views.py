from django.shortcuts import render

# Create your views here.
def showindex(request):
    return render(request,"index.html")
def register(request):
    id=request.GET.get("update_id")
    if id==None:
       from firebase import firebase as fab
       fa = fab.FirebaseApplication("https://employee-23752.firebaseio.com/informationdetails", None)
       d1= fa.get("informationdetails/",None)
       key=0
       if d1==None:
           key=201
       else:
           for x in d1:
               key=x
           key=(int(key)+1)
           return render(request,"register.html",{"key":key})

    else:
        from firebase import firebase as fab
        fa = fab.FirebaseApplication("https://employee-23752.firebaseio.com/informationdetails", None)
        e = fa.get("informationdetails/",id)
       #return render(request, "register.html")
        return render(request,"register.html",{"key":id,"name":e["name"],"cno":e["cno"]})
def viewdetails(request):
    from firebase import firebase as fab
    fa = fab.FirebaseApplication("https://employee-23752.firebaseio.com/informationdetails", None)
    emp=fa.get("informationdetails/",None)
    return render(request,"view.html",{"res":emp})
def savedetails(request):
    id=request.POST.get("id")
    name=request.POST.get("name")
    cno=request.POST.get("cno")
    d1={"name":name,"cno":cno}
    from firebase import firebase as fab
    fa=fab.FirebaseApplication("https://employee-23752.firebaseio.com/",None)
    fa.put("informationdetails",id,d1)
    return render(request,"register.html",{"message":"successfully saved your data in firebase"})
def deletedetails(request):
    id=request.POST.get("delete_id")
    from firebase import firebase as fab
    fa = fab.FirebaseApplication("https://employee-23752.firebaseio.com/informationdetails", None)
    emp = fa.delete("informationdetails/",id)
    return viewdetails(request)