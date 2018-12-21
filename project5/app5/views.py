from django.shortcuts import render

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def display(request):
    name=request.POST.get("lang")
    return render(request,"index.html",{"msg":name})


def displaymulti(request):
    name=request.POST.getlist("langs")
    print(name)
    return render(request,"index.html",{"mes":name})