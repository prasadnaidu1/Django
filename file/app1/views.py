from django.shortcuts import render

# Create your views here.
def showindex(request):
    return render(request,"index.html")


def displaydetails(request):
    file=request.POST.get("file")
    return render(request,"index.html",{"msg":file})