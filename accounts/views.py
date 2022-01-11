from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.http import HttpResponse

@login_required(login_url='accounts:login')
def home(request):
    user = request.user
    if user.gender == 0:
        gender = 'Male'
    elif user.gender == 1:
        gender = 'Female'
    else:
        gender = 'Other'
    return render(request, 'accounts/home.html', {
        'user': user, 
        'gender': gender})

def signup_view(request):
    if request.method == 'POST':
         form = CustomUserCreationForm(request.POST)
         if form.is_valid():
             user = form.save()
             #  log the user in
             login(request, user)
             return redirect('taskboard:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
               return redirect('taskboard:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

@login_required(login_url='accounts:login')
def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return redirect('accounts:login')