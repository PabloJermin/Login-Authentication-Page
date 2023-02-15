from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, "auths/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('FirstName')
        lname = request.POST.get('LastName')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.fname = fname
        myuser.lname = lname
        
        myuser.save()
        
        messages.success(request, "You've succesfully created an account")
        
        return redirect('signin')
    
    
    return render (request, "auths/signup.html")




def signin(request):
    if request.method == "POST":
        username = request.Post.get('username')
        password = request.Post.get('pass1')
        
        user = authenticate(username= username, password= pass1)
        
        if user is not None:
            login(request, user)
            fname = user.fname
            return render(request, "aunthentication/index.html", {'fname': fname})
        
        else:
            messages.error(request, "You entered a wrong email or password")
            return redirect('signin')
    
    
    
    
    return render (request, "auths/signin.html")




def signout(request):
    pass