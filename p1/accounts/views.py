from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):

    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password= request.POST['confirm_password']
        email = request.POST['email']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
            elif User.objects.filter(email=email).exist():
                messages.info(request, 'Email Taken')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')

        else:
            print('password unmached')    

        
        
        return redirect('/')
    else:

        return render(request, 'register.html')

