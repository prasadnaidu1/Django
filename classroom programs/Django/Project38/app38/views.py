from django.shortcuts import render

# Create your views here.
def showIndex(request):

    value = True
    #value = 1000

    return render(request,"index.html",{"value":value})