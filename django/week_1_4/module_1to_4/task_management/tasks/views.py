from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
  return render(request, 'home.html')
""" def manager_dashboard(request):
  return render(request, 'dashboard/manager_dashboard.html')
def user_dashboard(request):
  return render(request, 'dashboard/user_dashboard.html') """
def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")


def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test(request):
  context={
    "para":{
      "lorem ipsum dolor sit amet, consectetur adipiscing"
    }
  }
  return render(request, "test.html",context)

def showTask(request):
  return HttpResponse("<h2>Show Task</h2>")

def create_task(request):
  return render(request,"task_form.html")