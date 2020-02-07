from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.


def login (request):
    form =AuthenticationForm();
    return render(request,'auth/login.html',{'title':'Login','form':form})


def register (request):
       form =UserCreationForm();
       if request.method =='POST':
           form=UserCreationForm(request.POST);
           if form.is_valid():
               form.save()
       return render(request,'auth/register.html',{'title':'Registration','form':form})