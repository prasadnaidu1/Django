from django.shortcuts import render

def showindex(request):
    d1={'idno':101,
        'name':'prasad',
        'salary':100000.00 }
    return render(request,"index.html",{'emp':d1})
