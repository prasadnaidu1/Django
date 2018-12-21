from django.shortcuts import render

# Create your views here.
def showIndex(request):
    return render(request,"index.html")


def showType(request):
    uname = request.GET.get("t1")
    upass = request.GET.get("t2")

    return render(request,"index.html",{"mess":"Valid"})