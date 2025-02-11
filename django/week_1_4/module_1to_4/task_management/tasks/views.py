from django.shortcuts import render,redirect
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskModelForm,TaskDetailModelForm
from tasks.models import Task, TaskDetail, Project
from datetime import date
from django.db.models import Q,Count
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from users.views import is_admin, is_manager, is_employee
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.base import ContextMixin 
from django.views.generic import ListView,DetailView,UpdateView
# from functools import reduce


# class based view test
class MyView(View):
  def get(self,request):
    #view logic
    return HttpResponse("Response successfully")

class GreetingView(View):
  greeting = "Good Day" # Class attribute
  def get(self,request):
    # class Attribute 'greeting' ব্যবহার
    return HttpResponse(self.greeting)

class MorningGreetingView(GreetingView):
  greeting="Morning to ya" # subclass এ 'greeting' পরিবর্তন করা


@user_passes_test(is_manager)
def manager_dashboard(request):
  type = request.GET.get('type','all')
  tasks = Task.objects.select_related('details').prefetch_related('assigned_to').all()
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

#Todo should convert cbv manager dashboard 

@user_passes_test(is_employee)
def employee_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

#Todo should convert cbv manager dashboard 




@login_required
@permission_required("tasks.add_task",login_url='no-permission')
def create_task(request):
  task_form = TaskModelForm() #From Get
  task_detail_form = TaskDetailModelForm()
  if request.method == "POST":
    task_form = TaskModelForm(request.POST)
    task_detail_form = TaskDetailModelForm(request.POST,request.FILES)
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

# @method_decorator(login_required,name='dispatch')
# @method_decorator(permission_required("tasks.add_task",login_url='no-permission'),name='dispatch')

create_decorators = [
    login_required,
    permission_required("tasks.add_task", login_url='no-permission')
]

# @method_decorator(create_decorators, name="dispatch")
class CreateTask(ContextMixin,LoginRequiredMixin,PermissionRequiredMixin,View):
    permission_required = 'tasks.add_task'
    login_url = 'sign-in'
    template_name = "task_form.html"

    def get_context_data(self,**kwargs):
      context = super().get_context_data(**kwargs)
      context ['task_form']=kwargs.get('task_form',TaskModelForm())
      context['task_detail_form'] = kwargs.get('task_detail_form',TaskDetailModelForm())
      return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request,self.template_name, context)

    def post(self, request, *args, **kwargs):
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailModelForm(request.POST, request.FILES)
        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()
            messages.success(request, "Task Created Successfully")
            context = self.get_context_data(task_form = task_form,task_detail_form=task_detail_form)
            return render(request,self.template_name,context)

@login_required
@permission_required("tasks.view_task",login_url='no-permission')
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
  # use prefetch related fun
  return render(request,"show_task.html",{
    'tasks1':tasks1,
    'tasks2':tasks2,
    'tasks3':tasks3,
    'tasks4':tasks4,

  })

#Todo should convert cbv view task 


@login_required
@permission_required("tasks.change_task",login_url='no-permission')
def update_task(request,id):
  task = Task.objects.get(id=id)
  task_form = TaskModelForm(instance=task) # For GET

  if task.details:
    task_detail_form = TaskDetailModelForm(instance=task.details)
  if request.method == 'POST':
    task_form = TaskModelForm(request.POST,instance=task)
    task_detail_form = TaskDetailModelForm(request.POST,request.FILES,instance=task.details)
    
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


class UpdateTask(UpdateView):
  model = Task
  form_class = TaskModelForm
  template_name = 'task_form.html'
  context_object_name = 'task'
  pk_url_kwarg = 'id'

  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    context['task_form'] = self.get_form()
    print(context)
    if hasattr(self.object,'details') and self.object.details:
      context['task_detail_form'] = TaskDetailModelForm(
        instance = self.object.details
      )
    else:
      context['task_detail_form'] = TaskDetailModelForm()
    return context

  def post(self,request,*args, **kwargs):
      self.object = self.get_object()
      task_form = TaskModelForm(request.POST,instance=self.object)

      task_detail_form = TaskDetailModelForm(
        request.POST, request.FILES, instance=getattr(self.object, 'details', None)
      )
      if task_form.is_valid() and task_detail_form. is_valid():
        task = task_form.save()
        task_detail = task_detail_form.save (commit=False)
        task_detail.task = task
        task_detail.save()
        messages.success(request,"Task Updated  Successfully")
        return redirect('update-task',self.object.id)
      return redirect('update-task',self.object.id)




@login_required
@permission_required("tasks.delete_task",login_url='no-permission')
def delete_task(request,id):
  if request.method == "POST":
    task = Task.objects.get(id=id)
    task.delete()
    messages.success(request,'Task Deleted Successfully')
    return redirect('manager-dashboard')
  else:
    messages.error(request,'Something went wrong')
    return redirect('manager-dashboard')

#Todo should convert cbv delete task 

@login_required
def dashboard(request):
  if is_admin(request.user):
    return redirect('admin-dashboard')
  elif is_manager(request.user):
    return redirect('manager-dashboard')
  elif is_employee(request.user):
    return redirect('user-dashboard')
  return redirect('no-permission')


# @permission_required("tasks.view_task",login_url='no-permission')
def task_details(request, task_id):
    print(task_id)
    task = Task.objects.get(id=task_id)
    status_choices = Task.STATUS_CHOICES

    if request.method == 'POST':
        selected_status = request.POST.get('task_status')
        print(selected_status)
        task.status = selected_status
        task.save()
        return redirect('task-details', task.id)

    return render(request, 'task_details.html', {"task": task, 'status_choices': status_choices})

class TakDetails(DetailView):
    model = Task
    template_name = "task_details.html"
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'

    def get_context_data(self,**kwargs):
      context = super().get_context_data(**kwargs)
      context['status_choices'] = Task.STATUS_CHOICES
      return context
    
    def post(self, request, *args, **kwargs):
      task = self.get_object()
      selected_status = request.POST.get('task_status')
      task.status = selected_status
      task.save()
      return redirect('task-details', task.id)


class ViewProject(ListView):
  model = Project
  context_object_name = 'projects'
  template_name = 'show_task_2nd.html'
  def get_queryset(self):
    queryset = Project.objects.annotate(
      num_task=Count('task')
    ).order_by('num_task')
    return queryset