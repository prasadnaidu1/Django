from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Employee

class EmployeeReg(CreateView):
    model = Employee
    template_name = "register.html"
    fields = ['Name','Age','Contact','Salary']

    def form_valid(self, form):
        form.save()
        return HttpResponse("Valid")

    def form_invalid(self, form):
        return HttpResponse("Invalid")

