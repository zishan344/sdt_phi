from django.shortcuts import render,redirect
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm,TaskDetailModelForm
from tasks.models import Task, Employee, TaskDetail
from datetime import date
from django.db.models import Q,Count
from django.contrib import messages


# Create your views here.
def home(request):
  return render(request, 'home.html')
""" def manager_dashboard(request):
  return render(request, 'dashboard/manager_dashboard.html')
def user_dashboard(request):
  return render(request, 'dashboard/user_dashboard.html') """
def manager_dashboard(request):
  # tasks = Task.objects.all()
  type = request.GET.get('type','all')
  print(type)
  tasks = Task.objects.select_related('details').prefetch_related('assigned_to').all()
  
  # # getting task count
  # total_task =tasks.count()
  # completed_task = Task.objects.filter(status="COMPLETED").count()
  # in_progress_task = Task.objects.filter(status="IN_PROGRESS").count()
  # pending_task = Task.objects.filter(status="PENDING").count()
   
  counts = Task.objects.aggregate(
    total= Count('id'),
    completed= Count('id',filter=Q(status="COMPLETED")),
    in_progress= Count('id',filter=Q(status="IN_PROGRESS")),
    pending= Count('id',filter=Q(status="PENDING")),
  )

  # ! Retrieving task data
  base_query = Task.objects.select_related('details').prefetch_related('assigned_to')
  if type =='completed':
    tasks = base_query.filter(status='COMPLETED')
  elif type == 'in_progress':
    tasks = base_query.filter(status='IN_PROGRESS')
  elif type == 'pending':
    tasks = base_query.filter(status='PENDING')
  elif type =='all':
    tasks = base_query.all()

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
  task_form = TaskModelForm() #From Get
  task_detail_form = TaskDetailModelForm()
  # form = TaskForm(employees=employees) #From Get
  if request.method == "POST":
    task_form = TaskModelForm(request.POST)
    task_detail_form = TaskDetailModelForm(request.POST)
    if task_form.is_valid() and task_detail_form.is_valid():
      # for model form
      task = task_form.save()
      task_detail = task_detail_form.save(commit=False)
      task_detail.task = task
      task_detail.save()
      messages.success(request, "Task Created Successfully")
      return redirect('create-task')

  context = {"task_form": task_form,"task_detail_form":task_detail_form}
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

def update_task(request,id):
  task = Task.objects.get(id=id)
  task_form = TaskModelForm(instance=task) # For GET

  if task.details:
    task_detail_form = TaskDetailModelForm(instance=task.details)
  if request.method == 'POST':
    task_form = TaskModelForm(request.POST,instance=task)
    task_detail_form = TaskDetailModelForm(request.POST,instance=task.details)
    
    if task_form.is_valid() and task_detail_form.is_valid():
      task = task_form.save()
      task_detail = task_detail_form.save(commit=False)
      task_detail.task = task
      task_detail.save()
      messages.success(request,"Task Updated Successfully")
      return redirect('update-task',id)
  context = {
    "task_form":task_form,
    "task_detail_form":task_detail_form
  }
  return render(request,"task_form.html",context)

def delete_task(request,id):
  if request.method == "POST":
    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request,'Task Deleted Successfully')
    return redirect('manager-dashboard')
  else:
    messages.error(request,'Something went wrong')
    return redirect('manager-dashboard')
