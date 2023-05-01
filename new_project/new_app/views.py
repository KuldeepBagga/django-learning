from django.shortcuts import render
from django.http import HttpRequest
from new_app import forms
# Create your views here.
def index(request):
    return render(request,'index.html',{"title":"Home page"})

def register(request):
    studentregister=forms.RegisterName()
    
    if request.method=='POST':
        print("post")
        studentregister=forms.RegisterName(request.POST)
        if studentregister.is_valid():
            print("valid form")
    
    data={
        "title":"welcome to register page",
        "form":studentregister
    }
            
    return render(request,"register.html",data)