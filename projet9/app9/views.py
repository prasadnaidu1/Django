from django.shortcuts import render

def  ShowEmployee(request):
    d1={"101":{"name":"prasad","sal":185000.00},
        "102":{"name":"raju","sal":250000.00},
        "103": {"name": "rani", "sal": 50000.00},
        "104": {"name": "sekhar", "sal": 185000.00},
        "105": {"name": "kumar", "sal": 250000.00},
        "106": {"name": "raja", "sal": 50000.00}
    }
    return render(request,"employee.html",{"emp":d1})
