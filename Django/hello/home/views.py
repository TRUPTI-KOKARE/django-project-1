from django.shortcuts import render,HttpResponse
from home.models import Feedback
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')
   # return HttpResponse("this is Home page")def index(reques
def contact(request):
    return render(request,'contact.html')
def pythond(request):
    return render(request,'pythond.html')  
def pythonat(request):
    return render(request,'pythonat.html')
def pythonmt(request):
    return render(request,'python.html')
def verbal(request):
    return render(request,'verbal.html')
def apti(request):
    return render(request,'apti.html')   
def feedback(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        desc=request.POST.get('desc')
        feedback=Feedback(name=name,email=email,phno=phno,desc=desc)
        feedback.save()
    return render(request,'feedback.html')

 

