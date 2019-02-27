from django.shortcuts import render,HttpResponse
from .forms import Employment_Application
import random
# Create your views here.
def index(request): # one function only
    if (request.method=='POST'):   #If there is a post request
        x=random.randint(1,1000)   #I decided to add something extra because this assignment was way too easy
        context={
            'Name':request.POST['name'],
            'DOB':request.POST['date_Of_Birth'],
            'Salary':request.POST['salary'],
            'Position':request.POST['position'],
            'Number':x

        }
        return render (request,'cwApp/submitted.html',context)   #Go to the submitted applications page

    else:   #otherwise
        jobForm = Employment_Application()  #calls the job application from .forms
        context ={     #imports the job form
            'jobForm':jobForm,
        }
        return render(request,'cwApp/application.html',context)  #Go get a job