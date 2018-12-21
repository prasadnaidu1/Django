from django.shortcuts import render

def assign(request):
    dict={"director":
              {"principal":
                   {"101":{"name":"prasad","sal":120000}
                    },
              "head of department":
                   {"104":{"name":"avinash","sal":140000},
                    "105":{"name":"ravi","sal":16000}
                    },
              "faculity":
                   {"106":{"name":"kumar","sal":30000},
                    "107":{"name":"ravikumr","sal":70000},
                    "108":{"name":"raju","sal":400000},
                    "109":{"name":"raja","sal":73890}
                    },
              "receptionist":
                   {"110":{"name":"shanthi","sal":8900},
                    "111":{"name":"prasad","sal":80000}
                    },
              "attender":
                   {"112":{"name":"sampath","sal":60000}
                    }


              }
    }
    return render(request,"sample.html",{"college":dict})
