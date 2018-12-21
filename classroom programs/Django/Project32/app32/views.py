from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


def showIndex(request):
    return render(request,"index.html")


class Sample(View):

    def get(self,request):
        return HttpResponse("Clicked on Get Button")

    def post(self,request):
        return HttpResponse("Clicked on Post Button")