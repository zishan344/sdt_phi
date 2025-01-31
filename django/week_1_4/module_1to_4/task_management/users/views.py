from django.shortcuts import render, redirect
from users.form import RegisterForm,CustomRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def sign_up(request):
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
          # username = form.cleaned_data.get('username')
          # password = form.cleaned_data.get('password1')
          # confirm_password = form.cleaned_data.get('password2')
          
          # if password == confirm_password:
          #   User.objects.create(username=username, password=password)
          # else:
          #   print("Password are not same")
          form.save()
        else:
          print("Form is not valid")
    else:
        form = CustomRegistrationForm()

    return render(request, 'registration/register.html', {"form": form})

def sign_in (request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user =authenticate(username=username, password=password)
    if user is not None:
      login(request,user)
      return redirect('home')
    else:
      return render(request,'registration/login.html',{
        'error':'Invalid username or password'
      })
  return render(request,'registration/login.html')
  
def sign_out(request):
  if request.method == 'POST':
    logout(request)
    return redirect('sign-in')