from django import forms


class EmployeeReg(forms.Form):
    name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    cno = forms.IntegerField()
