from django.shortcuts import render
from firebase import firebase as fab

def showindex(request):
    fa = fab.FirebaseApplication("https://loginpage-9f66f.firebaseio.com/login",None)
    d1 = {"details": {"developer": {"101": {"name": "prasad", "sal": 89000},
                                    "102": {"name": "jagga", "sal": 79000}
                                    },
                      "tester":
                          {"104": {"name": "vamsi", "sal": 99000},
                           "105": {"name": "ravi", "sal": 100000}
                           }
                      }
          }
    d2=fa.put("https://loginpage-9f66f.firebaseio.com/login/","employeedetails",None,d1)

    return render(request,"index.html")
