from django.shortcuts import render

def showindex(request):
    employee={"developer":
                 {"morning":
                      {"101":{"name":"prasad","sal":120000},
                       "102":{"name":"raju","sal":130000}
                       },

                 "evening":
                      {"104":{"name":"raja","sal":300000},
                       "105":{"name":"rani","sal":38000}
                       }
                  },
             "tester":
                 {"morning":
                       {"106":{"name":"ravi","sal":134000},
                       "107":{"name":"kumar","sal":40000}
                       },

                 "evening":
                        {"107":{"name":"kumar","sal":5000000},
                         "108":{"name":"ravikumar","sal":89090}
                         }
                 },
             "designer":{"109":{"name":"niranjan","sal":6000000}
                        }
     }


    return render(request,"employee.html",{"emp":employee})





