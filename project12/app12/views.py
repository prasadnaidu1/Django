from django.shortcuts import render

def dispaly(request):
    dictionary={'departments':
                    {'marketing':
                         {'morning':
                              {'101':
                                   {'name':'prasad','sal':120000},
                               '102':{'name':'raju','sal':30000}
                               },
                          'evening':
                              {'103':{'name':'raja','sal':60000},
                               '104':{'name':'raj','sal':323949}
                               }
                          },
                     'financial':
                         {'morning':
                              {'105':{'name':'ravi','sal':130000},
                               '106':{'name':'chandhu','sal':40000}
                               },
                          'evening':
                              {'107':{'name':'kumar','sal':50000},
                               '108':{'name':'ramesh','sal':60000}
                               },
                          },
                     'manufacturing':
                         {'morning':
                              {'109':{'name':'ravikumar','sal':89000}
                               }
                          }
                     }
                }
    return render(request,"dict.html",{'emp':dictionary})
