from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('articles:list')  
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form })

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
               return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def user_profile(request):
    user = request.user
    print("is_manager:", user.is_manager)
    print("is_coordinator:", user.is_coordinator)

def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return redirect('articles:list')
    
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})
    
