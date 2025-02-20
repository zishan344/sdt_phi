from django.shortcuts import render, redirect


# Create your views here.


def home (request):
  return render(request, 'homes.html')

def no_permission (request):
  return render(request, 'no_permission.html')