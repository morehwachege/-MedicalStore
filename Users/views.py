from django.shortcuts import redirect, render
from Users.forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def create_user(request):
     form = CreateUserForm()
     if request.method =='POST':
         form = CreateUserForm(request.POST or None)
         if form.is_valid():
             form.save()
             user = form.cleaned_data.get('username')
             messages.success(request, "Account Created for "+ user)
             return redirect('login')
     else:
        form = CreateUserForm()
     context={
        'form':form
    }
     return render(request, "Users/register.html", context)

   
def user_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('medList')
        else:
            messages.info(request, "username or password is incorrect")
    return render(request, "Users/login.html")

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')
