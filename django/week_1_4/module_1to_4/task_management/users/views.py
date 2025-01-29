from django.shortcuts import render, redirect
from users.form import RegisterForm
from django.contrib.auth.models import User

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
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
        form = RegisterForm()

    return render(request, 'registration/register.html', {"form": form})
