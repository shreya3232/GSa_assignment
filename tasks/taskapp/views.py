# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm, TaskForm
from .models import *


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Implement login logic here
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Implement address fetching from Google Maps and saving to DB
            user = form.save(commit=False)
            user.latitude = 0.0  # Replace with latitude fetched from Google Maps
            user.longitude = 0.0  # Replace with longitude fetched from Google Maps
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def dashboard(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    form = TaskForm()
    users = User.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('dashboard')

    return render(request, 'dashboard.html', {'tasks': tasks, 'form': form, 'users': users})