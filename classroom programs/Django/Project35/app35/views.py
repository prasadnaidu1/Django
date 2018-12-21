
from django.shortcuts import render
from django.views.generic import View,ListView,DeleteView

from .models import ContactsInfo

class SaveContacts(View):

    def post(self,request):
        name = request.POST.get("t1")
        cno = request.POST.get("t2")
        ci = ContactsInfo(name=name,cno=cno)
        ci.save()
        return render(request,"index.html",{"mess":"Saved"})

class ViewContacts(ListView):
    queryset = ContactsInfo.objects.all()

class ViewOneContact(DeleteView):
    model = ContactsInfo
    queryset = ContactsInfo.objects.filter(cno=9052492329)