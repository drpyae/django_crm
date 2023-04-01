from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def home(request):
    # Check to see if loggin in
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username =user_name, password = password)
        if user is not None:
            login(request, user)
            message.success(request, "You have succesfully Logged In")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, please try again.")
    else:
        return render(request, 'home.html',{})
            
    return render(request, 'home.html',{})
def login_user(request):
    pass
def logout_user(request):
    pass