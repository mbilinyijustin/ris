from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
# Create your views here.

def mbilinyi(request):
    if request.method=="POST":
        username=request.POST["username"]
        email=request.POST['email']
        password=request.POST['password']
        student=Student(username=username, email=email, password=password)
        student.save()


    










       #return HttpResponse('Hello world!')
    return render(request, ('index.html'))
