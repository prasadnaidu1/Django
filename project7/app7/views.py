from django.shortcuts import render
def show (request):
    d1={'idno':1010,
        'name':'prasad',
        'salary':1200000.0}
    return render(request,"show.html",{'emp':d1})

