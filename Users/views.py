from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib import messages

def home(request):
    return render(request, 'Users/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return render(request, 'Users/login.html')
        else:
            form = UserRegistrationForm() 
    return render(request, 'Users/register.html')
        
        
# @login_required
def Profile(request):
    if request == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance= request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile successfully updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance= request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'Users/profile.html', context)


def login(request):
    return render(request, 'Users/login.html')