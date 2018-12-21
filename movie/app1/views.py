from django.shortcuts import render
NTR=["temper","lavakusa","aravindha","prasad"]
Balaiah=["simha","legend","prasad"]
Kalyanram=["patas","ism","prasad"]

def showindex(request):
    return render(request,"index.html")

def moviedetails(request):
    hero=request.POST.get("hero")
    print(hero)
    if hero=="NTR":
        return render(request,"index.html",{"movie":NTR})
    elif hero=="Balaiah":
        return render(request,"index.html",{"movie":Balaiah})
    elif hero=="Kalyanram":
        return render(request,"index.html",{"movie":Kalyanram})


def posters(request):
    poster=request.POST.getlist("movies")
    print(poster)
    return render(request,"index.html",{"posters":poster})