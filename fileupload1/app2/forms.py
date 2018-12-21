from django import forms
class student(forms.Form):
    name=forms.CharField(label="Student Name:",max_length=50)
    cno=forms.IntegerField(label="Contact No:")
    file=forms.FileField()