from django.shortcuts import render,redirect


def openFB(request):
    return  redirect("http://www.facebook.com")

from django.views.generic import RedirectView

class OpenGoogle(RedirectView):
    url = "http://www.google.com"