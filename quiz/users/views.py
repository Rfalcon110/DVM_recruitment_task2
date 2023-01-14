from django.shortcuts import render,redirect
from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register') 
    else:
        form=UserCreationForm()
        return render(request,'users/register.html',{'form':form})   
def home(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return redirect('login')
 
def logoutPage(request):
    logout(request)
    return redirect('/')
#def register_as_qm(request):
def register_as_admin(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        
        password=form.password1
        if form.is_valid():
            username=form.username
            user=User.objects.create_user(username,password=password)
            user.user_permissions.add('quizapp.add_quiz','quizapp.view_quiz','quizapp.change_quiz','quizapp.delete_quiz',)
            user.save()
            login(request,user)
            return redirect('login')
        else:
            return redirect('register') 
    else:
        form=UserCreationForm()
        return render(request,'users/register.html',{'form':form})    