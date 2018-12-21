from django.shortcuts import render

from app41.forms import EmployeeReg

def showIndex(request):
    emp = EmployeeReg()
    return render(request,"index.html",{"employee":emp})