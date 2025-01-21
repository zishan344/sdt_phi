from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm
from tasks.models import Task, Employee, TaskDetail
from datetime import date
from django.db.models import Q
# Create your views here.
def home(request):
  return render(request, 'home.html')
""" def manager_dashboard(request):
  return render(request, 'dashboard/manager_dashboard.html')
def user_dashboard(request):
  return render(request, 'dashboard/user_dashboard.html') """
def manager_dashboard(request):
  tasks = Task.objects.all()
  
  # # getting task count
  total_task =tasks.count()
  completed_task = Task.objects.filter(status="COMPLETED").count()
  in_progress_task = Task.objects.filter(status="IN_PROGRESS").count()
  pending_task = Task.objects.filter(status="PENDING").count()

  counts = {
    "tasks":tasks,
    "total": total_task,
    "completed": completed_task,
    "in_progress": in_progress_task,
    "pending": pending_task
  }
  context= {
    "tasks": tasks,
    "counts": counts
  }
  return render(request, "dashboard/manager-dashboard.html",context)


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


def view_task(request):
  # tasks = Task.objects.all()
  # tasks = Task.objects.filter(status="PENDING")

  # retrieve task with due date in today 
  # tasks = Task.objects.filter(due_date=date.today())

  # exclude with priority based
  # tasks = TaskDetail.objects.exclude(priority="H")
  # ! show tasks that contain word paper
  tasks1 = Task.objects.filter(title__icontains="paper")

  #! show tasks that contain latter 'c' and also status is 'Pending'
  tasks2 = Task.objects.filter(title__icontains="c",status="PENDING")

  # !show the tasks which are PENDING or IN-PROGRESS
  tasks3 = Task.objects.filter(Q(status="PENDING") | Q(status="IN-PROGRESS"))

  # !check the task exists or not
  tasks4 = Task.objects.filter(status="adfsdskfd").exists()

  # ! use select related fun
  tasks = Task.objects.prefetch_related('assigned_to').all()
  print("tasks =: ",tasks)
  for task in tasks:
    print(task.assigned_to.all())
  """
  tasks = Task.objects.select_related('project').all()
  for task in tasks:
    print(task.project.name)

  """
  
  


  # use prefetch related fun
  
  return render(request,"show_task.html",{
    'tasks1':tasks1,
    'tasks2':tasks2,
    'tasks3':tasks3,
    'tasks4':tasks4,

  })
