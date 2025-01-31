from django.shortcuts import render, redirect
from users.forms import RegisterForm,CustomRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from users.forms import LoginForm
from django.contrib.auth.tokens import default_token_generator
from users.forms import LoginForm

def activate_user(request,user_id, token):
  try:
    user = User.objects.get(id = user_id)
    if default_token_generator.check_token(user, token):
      user.is_active = True
      user.save()
      return redirect('sign-in')
    else:
      return HttpResponse('Invalid Id or token')
  except User.DoesNotExist:
      return HttpResponse('User not found')

def sign_up(request):
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
          user = form.save(commit=False)
          user.set_password(form.cleaned_data.get('password1'))
          user.is_active = False
          user.save()
          messages.success(request,'A Confirmation mail send. Please Check your email')
          return redirect('sign-in')
        else:
          print("Form is not valid")
    else:
        form = CustomRegistrationForm()

    return render(request, 'registration/register.html', {"form": form})

def sign_in (request):
  form = LoginForm()
  if request.method == 'POST':
    form = LoginForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request,user)
      return redirect('home')
  return render(request,'registration/login.html')
  
def sign_out(request):
  if request.method == 'POST':
    logout(request)
    return redirect('sign-in')