from django.http import HttpResponse
def display(request):
    return HttpResponse('<h1>Hello Django</h1> <h2>This is Django Sample Program</h2>')