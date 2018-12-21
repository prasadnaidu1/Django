from django.shortcuts import render
def showindex(request):
    return render(request,"index.html")
def display(request):
    Fname = request.POST.get("t1")
    Mname = request.POST.get("t2")
    Lname = request.POST.get("t3")
    Pass = request.POST.get("t4")
    Cno = request.POST.get("t5")
    Email = request.POST.get("t6")
    Adds = request.POST.get("t8")
    Pin = request.POST.get("t9")
    DB = request.POST.get("t10")
    d1={"fname":Fname,"mname":Mname,"lname":Lname,"pass":Pass,"email":Email,"adds":Adds,"pin":Pin,"date of birth":DB}
    from firebase import firebase as fab
    fa = fab.FirebaseApplication("https://student-5f369.firebaseio.com",None)
    fr = fa.put("https://student-5f369.firebaseio.com/details",Cno,d1)
    f_get=fr.get("https://student-5f369.firebaseio.com/details",None)
    return render(request,"index.html",{"emp":f_get,"message":"successfully saved"})


