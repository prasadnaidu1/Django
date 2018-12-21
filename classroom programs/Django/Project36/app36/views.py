from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView

from .models import Student

class StudentRegister(CreateView):
    model = Student
    template_name = "student_register.html"
    fields = ['Name','Age','Contact','Email','Password']

    def form_valid(self, form):
        form.save()
        return HttpResponse("Registred")

    def form_invalid(self, form):
        return HttpResponse("Not-Registred")