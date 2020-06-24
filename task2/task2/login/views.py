from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm

def logoutUser(request):
    logout(request)
    return redirect('signup')
        


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
            return redirect('home')
    else:
        form = SignUpForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'registration/signup.html', {'form': form}) 