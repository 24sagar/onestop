from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Replace 'home' with the name of your homepage URL pattern
    else:
        form = AuthenticationForm()
    return render(request, "login_view.html", {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Replace 'home' with the name of your homepage URL pattern
    else:
        form = UserCreationForm()
    return render(request, "signup_view.html", {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to homepage after logout

