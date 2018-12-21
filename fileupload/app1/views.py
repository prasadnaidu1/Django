from app1.functions.functions import upload_file
from django.http import HttpResponse
from django.shortcuts import render
from app1.forms import student

def showindex(request):
    if request.method=="POST":
        sf=student(request.POST,request.FILES)
        print(sf)
        if sf.is_valid():
            upload_file(request.FILES['file'])
            return HttpResponse("file uploaded")
    else:
        Student=student()
        return render(request,"index.html",{"form":Student})
