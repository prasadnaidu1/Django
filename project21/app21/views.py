from django.shortcuts import render

def showindex(request):
    return render(request,"index.html")
def dispaly(request):
    name = request.POST.get("t1")
    age = request.POST.get("t2")
    email = request.POST.get("t3")
    cno=request.POST.get("t4")


    d1={"name":name,"age":age,"emial":email}
    from firebase import firebase as fab
    fa=fab.FirebaseApplication("https://student-5f369.firebaseio.com/",None)
    fr = fa.put("https://student-5f369.firebaseio.com/companydetails",cno,d1)
    f_get = fa.get("https://student-5f369.firebaseio.com/companydetails",None)
    return  render(request,"index.html",{"emp":f_get,"message":"successfully saved"})


