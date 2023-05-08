

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ...models import CustomUser
import datetime
from ...form import userRegistrationForm,userLoginForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
def home(request):
    return render(request,'registration/home.html')
def signup(request):
    if request.method == 'POST':
        # first_name = request.POST['first_name']
        # last_name = request.POST['first_name']
        
        registration_no = request.POST.get('registration_no')
        email = request.POST.get('email')        # dept_name = request.POST['dept_name']
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        print(password,confirm_password)
        # roll = request.POST['roll']
        # session = request.POST['session']

        if password == confirm_password:
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'email already exists')
                return redirect('/signup')
            elif CustomUser.objects.filter(registration_no=registration_no).exists():
                messages.error(
                    request, 'you are already registered by your registration number')
                return redirect('/signup')
            else:
                user = CustomUser(
                    registration_no=registration_no, email=email, password=make_password(password),date_joined=datetime.datetime,last_login=datetime.time,is_active=True,is_admin=False,is_superuser=False,is_staff=False)
                user.save()
                authenticate_user = authenticate(registration_no=registration_no,password=password)
                authenticate_user.save()
                
                messages.success(request, 'user saved successfully')

        else:
            messages.error(request, 'password do not match')
            return redirect('/signup')
    else:
        return render(request, 'registration/signup.html')

    return render(request, 'registration/login.html')

def login_view(request):
    if request.method == 'POST':
        registration_no = request.POST.get('registration_no')
        print('r',registration_no)
        password = request.POST.get('password')
        print('s',password)
        user = authenticate( registration_no=registration_no, password=password)
        if user is not None:
            print('1')
            login(request, user)
            return render(request,'registration/home.html')
        else:
            print('2')
            error_message = "Invalid login credentials"
    else:
        error_message = None
        print(error_message,'3')
    return render(request, 'registration/login.html', {'error_message': error_message})
