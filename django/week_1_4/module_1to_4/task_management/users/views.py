from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {"form": form})
