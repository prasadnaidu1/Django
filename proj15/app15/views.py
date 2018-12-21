from django.shortcuts import render

def showIndex(request):
    return render(request,"index.html")
def detailsshow(request):
    name=request.POST.get("t1")
    age=request.POST.get("t2")
    cno=request.POST.get("t3")
    email=request.POST.get("t4")
    sal=request.POST.get("t5")
    adds=request.POST.get("t6")
    d1={"name":name,"age":age,"cno":cno,"email":email,"sal":sal,"adds":adds}
    return  render(request,"details.html",d1)


