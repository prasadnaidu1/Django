from django.http import HttpResponse
from django.shortcuts import render
from .forms import student
from app2.functions.functions import upload_file
#from .models import student

# Create your views here.
def showindex(request):
    if request.method=="POST":
        sf=student(request.POST,request.FILES)
        if sf.is_valid():
            upload_file(request.FILES["file"])
            return HttpResponse("file uploaded successfully")
    else:
        s1=student()
        return render(request,"index.html",{"form":s1})


#def studentdetails(request):
   #details= request.POST.get("multipart/form-data")
   #student(details).save()
   #return render(request,"index.html",{"msg":"datasaved"})