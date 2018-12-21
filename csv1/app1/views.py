from django.http import HttpResponse
from django.shortcuts import render
import csv
# Create your views here.
def showindex(request):
    return render(request,"index.html")

def createcsv(request):
    response=HttpResponse(content_type="text/csv")
    response['Content-Disposition']='attachment';filename="employee.csv"
    wr=csv.writer(response)
    wr.writerow([101,'prasad','developer',125000.00])
    wr.writerow([102,'prasadnaidu','developer',185000.00])
    return response