# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# # Create your models here
# class customUserRegistrationManager(BaseUserManager):
#  def _create_user(self ,registration_no, email,password, confirm_password):
#   if not registration_no:
#    raise ValueError("The registration field must be set")
#   if not email :
#    raise ValueError("You haven't provided a valid email address")
#   if not password:
#    raise ValueError("You haven't provided a pasword")
#   email = self.normalize_email(email)
#   user = self.model(registration_no=registration_no,email=email,password=password,confirm_password=confirm_password)
#   user.set_password(password)
#   user.save(using=self.db)
#   return user
 
#  def _create_super_user(self,registration_no,email,password,confirm_password);

# class userRegistration(AbstractBaseUser,PermissionsMixin):
#  registration_no = models.CharField(primary_key=True,max_length=15,unique=True)
#  email = models.EmailField(max_length=20,unique=True)
#  password = models.CharField(max_length=30)
#  confirm_password = models.CharField(max_length=30)
#  date_joined = models.DateTimeField(auto_now=True)
#  last_login = models.DateTimeField(auto_now=True)
#  is_active = models.BooleanField(default=True)
#  is_admin = models.BooleanField(default=False)
#  is_superuser = models.BooleanField(default=False)
#  is_staff = models.BooleanField(default=True)
#  is_verified = models.BooleanField(default=False)

#  USERNAME_FIELD =  'registration_no'
#  REQUIRED_FIELDS=['registrtation_no','email','password','confirm_password']

#  object = 

#  def __str__(self):
#   return self.registration_no
 
#  def has_perm(self, perm, obj=None) -> bool:
#   return True
 
#  def has_module_perms(self, app_label: str) -> bool:
#   return True
from django.db import models
from django import forms
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.contrib.auth.hashers import make_password

class CustomUserManager(BaseUserManager):
    def create_user(self, registration_no, email, password=None):
        if not registration_no:
            raise ValueError('Users must have a registration number')

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            registration_no=registration_no,
            email=self.normalize_email(email),
            # password=password,
            # is_verified = is_verified
        )

        user.set_password(make_password(password))
        user.save(using=self._db)
        return user

    def create_superuser(self, registration_no, email, password):
        user = self.create_user(
            registration_no=registration_no,
            email=email,
            password=password,
            # is_verified=is_verified
        )

        user.isadmin= True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser,PermissionsMixin):
    registration_no = models.CharField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField()
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'registration_no'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.registration_no

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Student(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)
    hall = models.CharField(max_length=100)
    email = models.EmailField()
    fathers_name = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    present_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    social_media_link_1 = models.CharField(max_length=100)
    social_media_link_2 = models.CharField(max_length=100, blank=True, null=True)
    ssc_institution = models.CharField(max_length=100)
    ssc_board = models.CharField(max_length=100)
    ssc_passing_year = models.IntegerField()
    hsc_institution = models.CharField(max_length=100)
    hsc_board = models.CharField(max_length=100)
    hsc_passing_year = models.IntegerField()
    photography = models.BooleanField(default=False)
    content_writing = models.BooleanField(default=False)
    debating = models.BooleanField(default=False)
    graphics_designing = models.BooleanField(default=False)
    web_development = models.BooleanField(default=False)
    hobbies_and_interests = models.CharField(max_length=100)
    why_join_duits = models.CharField(max_length=100)
    information_tech_interest = models.CharField(max_length=100)
    other_club_member = models.CharField(max_length=100)
    microsoft_word = models.BooleanField(default=False)
    microsoft_excel = models.BooleanField(default=False)
    adobe_illustrator_or_photoshop = models.BooleanField(default=False)
    canva = models.BooleanField(default=False)
    google_workspace = models.BooleanField(default=False)
    program_compilers = models.BooleanField(default=False)


    def __str__(self):
        return self.name
# class RegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = CustomUser
#         fields = [ 'email']

#     def clean(self):
#         cleaned_data = super(RegistrationForm, self).clean()
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')
#         if password != confirm_password:
#             raise forms.ValidationError("Passwords do not match")
#         return cleaned_data

# class LoginForm(forms.Form):
#     registration_no = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super(LoginForm, self).clean()
#         registration_no = cleaned_data.get('registration_no')
#         password = cleaned_data.get('password')
#         if registration_no and password:
#             user = authenticate(registration_no=registration_no, password=password)
#             if not user:
#                 raise forms.ValidationError("Invalid login credentials")
#         return cleaned_data
