# from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
# from django.contrib import messages, auth
# from .models import userRegistration

# # Create your views here.


# def signup(request):
#     if request.method == 'POST':
#         # first_name = request.POST['first_name']
#         # last_name = request.POST['first_name']
#         email = request.POST['email']
#         registration_no = request.POST['registration_no']
#         # dept_name = request.POST['dept_name']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
#         # roll = request.POST['roll']
#         # session = request.POST['session']

#         if password == confirm_password:
#             if userRegistration.objects.filter(email=email).exists():
#                 messages.info(request, 'email already exists')
#                 return redirect('signup/')
#             elif userRegistration.objects.filter(registration_no=registration_no).exists():
#                 messages.info(
#                     request, 'you are already registered by your registration number')
#                 return redirect('signup/')
#             else:
#                 user = userRegistration(
#                     registration_no=registration_no, email=email, password=password, confirm_password=confirm_password,is_verified=False)
#                 user.save()
#                 messages.info(request, 'user saved successfully')

#         else:
#             messages.info(request, 'password do not match')
#             return redirect('signup/')
#     else:
#         return render(request, 'registration/signup.html')

#     return render(request, 'registration/login.html')

# # login part


# def login(request):
#  if request.method=='POST':
#     registration_no = request.POST['registration_no']
#     password = request.POST['password']

#     user = auth.authenticate(registration_no=registration_no,password=password)
#     if user is not None :
#         auth.login(request,user)
#         return redirect('/signup')  
#     else:
#         messages.info(request, 'invalid username or password')
#         return redirect('/admin')
#  return render(request, 'registration/login.html')


# ggg

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser
import datetime
from .form import userRegistrationForm,userLoginForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .form import StudentForm
def home(request):
    return render(request,'registration/home.html')

def regisration(request):
    # if request.method == 'POST':
    #     current_step = int(request.POST.get('current_step'))

    #     if current_step == 1:
    #         form = StepOneForm(request.POST)
    #         if form.is_valid():
    #             request.session['step_one_data'] = form.cleaned_data
    #             return redirect('multi_step_form')

    #     elif current_step == 2:
    #         form = StepTwoForm(request.POST)
    #         if form.is_valid():
    #             request.session['step_two_data'] = form.cleaned_data
    #             return redirect('multi_step_form')

    #     elif current_step == 3:
    #         form = StepThreeForm(request.POST)
    #         if form.is_valid():
    #             request.session['step_three_data'] = form.cleaned_data
    #             # Do something with the form data...
    #             # For example, save the form data to a database
    #             step_one_data = request.session.get('step_one_data')
    #             step_two_data = request.session.get('step_two_data')
    #             step_three_data = request.session.get('step_three_data')
    #             # Reset the session data
    #             request.session['step_one_data'] = None
    #             request.session['step_two_data'] = None
    #             request.session['step_three_data'] = None
    #             messages.success(request, 'Form submitted successfully!')
    #             return redirect('multi_step_form')

    # else:
        # Initialize the form for the first step
    #     form = StepOneForm()

    # context = {
    #     'form': form
    # }
    # return render(request, 'registration/registration.html', context)
    # if request.method == 'POST':
    #     form = StudentForm(request.POST)
        
    #     if form.is_valid():
    #         form.save()
    #         return redirect('success')
    # else:
    #     form = StudentForm()

    # return render(request, 'registration/registration_form.html', {'form': form})
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your registration has been submitted!')
            return redirect('/home')
    else:
        form = StudentForm()

    context = {'form': form}
    return render(request, 'registration/registration_form.html', context)
def success(request):
    return render(request, 'registration/success.html')

def profile(request) :
    return render(request,'registration/profile.html')
def signup(request):
 if request.method == 'POST':
    registration_no = request.POST.get('registration_no')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    print(password, confirm_password)

    if password == confirm_password:
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('/signup')
        elif CustomUser.objects.filter(registration_no=registration_no).exists():
            messages.error(request, 'you are already registered by your registration number')
            return redirect('/signup')
        else:
            user = CustomUser(
                registration_no=registration_no,
                email=email,
                password=make_password(password),
                date_joined=datetime.datetime.now(),
                last_login=datetime.datetime.now(),
                is_active=True,
                is_admin=False,
                is_superuser=False,
                is_staff=False,
            )
            user.save()

            # Authenticate and login user
            authenticated_user = authenticate(request, registration_no=registration_no, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, 'User authenticated and logged in successfully')
            else:
                messages.error(request, 'Unable to authenticate user')

            return redirect('/')

    else:
        messages.error(request, 'password do not match')
        return redirect('/signup')

 else:
    return render(request, 'registration/signup.html')


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
            return redirect('/admin')
        else:
            print('2')
            error_message = "Invalid login credentials"
    else:
        error_message = None
        print(error_message,'3')
    return render(request, 'registration/login.html', {'error_message': error_message})
