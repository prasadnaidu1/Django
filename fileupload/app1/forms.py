from django import forms
class student(forms.Form):
    fname=forms.CharField(label="enter a first name",max_length=50)
    lname=forms.CharField(label="enater a second name",max_length=50)
    file=forms.FileField()
