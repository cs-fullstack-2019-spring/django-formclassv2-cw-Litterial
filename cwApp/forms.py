from django import forms
from django.utils import timezone  #apparently it does not use timezone
 #form for the job application
class Employment_Application(forms.Form):
    name=forms.CharField()
    date_Of_Birth=forms.DateField()
    position=forms.CharField()
    salary=forms.IntegerField()



