from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from LoginProject import settings
from django.core.mail import send_mail

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
        
        if User.objects.filter(username='usename'):
            messages.error(request, "Username already exist")
            return redirect('home')
        
        
        if User.objects.filter(email= 'email'):
            messages.error(request, "email already exist")
            return redirect('home')
        
        if len(username) > 10:
            messages.error(request, "username must be less than 10 characters")
            
        if pass1 != pass2:
            messages.error(request, "Sorry, the passwords do not much")
            
            
        if not username.isalnum():
            messages.error(request, "the username must be alphanumeric")
            return redirect ('home')
            
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.f_name = fname
        myuser.l_name = lname
        
        myuser.save()
        
        messages.success(request, "You've succesfully created an account. Please activate by confirming your acount")
        
        
    
        # WELCOMING EMAIL MESSAGE
        
        subject = "Welcome to this page"
        meessage = "hello " + myuser.f_name + "!," + "welcome to this website, \n\n Please click on the link to"
        "confirm your account"
        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently= True)
    
        return redirect('signin')
    
    return render(request, "auths/signup.html")



def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        
        user = authenticate(username=username, password= pass1)
        
        if user is not None:
            login(request, user)
            fname = user.username
            return render(request, "authentication/index.html", {'fname': fname})
        
        else:
            messages.error(request, "You entered a wrong email or password")
            return redirect('signin')
    
    return render(request, "authentication/signin.html")



def signout(request):
    logout(request)
    messages.success(request, "Logged out sucessfully")
    return render (resquest, 'authentication/index/html')