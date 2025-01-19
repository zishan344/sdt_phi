from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Task, Employee
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
  employees = Employee.objects.all()
  form = TaskModelForm() #From Get
  # form = TaskForm(employees=employees) #From Get
  if request.method == "POST":
    form = TaskModelForm(request.POST)
    if form.is_valid():
      # for model form
      form.save()
      return render(request,'task_form.html',{'form':form,"message":"Task added successfully"})
      # data= form.cleaned_data
      # title = data.get('title')
      # description = data.get('description')
      # due_date = data.get('due_date')
      # assigned_to = data.get('assigned_to')
      # task = Task.objects.create(
      #   title = title,description = description,due_date = due_date
      # ) 
      # for emp_id in assigned_to:
      #   employee = Employee.objects.get(id=emp_id)
      #   task.assigned_to.add(employee)

  context = {"form": form}
  return render(request,"task_form.html",context)