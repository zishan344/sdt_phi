from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
  return HttpResponse("Welcome to the task management system")
def contact(request):
  return HttpResponse("<h2>Welcome to the contact page</h2>")

def showTask(request):
  return HttpResponse("<h2>Show Task</h2>")
