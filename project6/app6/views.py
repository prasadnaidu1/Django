from django.shortcuts import render

# Create your views here.


def showindex(request):
    return render(request,"index.html")


def displaydetails(request):
    name=request.Post.get("hero")
    print(name)
    return  hero(request,name)
def hero(request,name):
    if name=="NTR":
        li=["Temper","Aravindhasametha","jai Lavakusa"]
        return render(request,"index.html",{"mli":li})
    elif name=="Balaiah":
        li=["Simha","Legend"]
        return render(request,"index.html",{"mli":li})
    elif name=="KalyanRam":
        li=["Patas"]
        return render(request,"index.html",{"mli":li})
    else:
        return None


def movie(request):
    mli=request.Post.getlist("movie")
    ili=tuple()
    for i in mli:
        if i=="Temper":
            ili=ili+("ntr1.jpg")
        elif i == "Aravindhasametha":
            ili = ili + ("ntr2.jpg")
        elif i=="jai Lavakusa":
            ili=ili+("ntr.jpg")
        elif i=="Simha":
            ili=ili+("download (13)")
        elif i=="Legend":
            ili=ili+("download (10)")
        elif i=="Patas":
            ili=ili+("download (14)")
    for x in ili:
        print(x)

    return render(request,"index.html",{"ili":ili})