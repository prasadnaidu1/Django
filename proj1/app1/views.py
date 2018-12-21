
from django.http import HttpResponse
def ShowHomePage(request):
    return  HttpResponse('<h1>      Hello                            Django </h1> <h2> Python</h2>')