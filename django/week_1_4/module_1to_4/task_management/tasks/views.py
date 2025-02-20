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
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic.base import ContextMixin 
from django.views.generic import ListView,DetailView,UpdateView,TemplateView,DeleteView
from django.urls import reverse_lazy

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
class ManagerDashboardView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    login_url = 'sign-in'
    model = Task
    template_name = "dashboard/manager-dashboard.html"
    context_object_name = "tasks"

    def test_func(self):
        return is_manager(self.request.user)

    def get_queryset(self):
        task_type = self.request.GET.get("type", "all")
        base_query = Task.objects.select_related("details").prefetch_related("assigned_to")

        if task_type == "completed":
            return base_query.filter(status="COMPLETED")
        elif task_type == "in_progress":
            return base_query.filter(status="IN_PROGRESS")
        elif task_type == "pending":
            return base_query.filter(status="PENDING")
        return base_query.all()  # Default: Show all tasks

    def get_context_data(self, **kwargs):
        """Add aggregated task counts to context."""
        context = super().get_context_data(**kwargs)
        context["counts"] = Task.objects.aggregate(
            total=Count("id"),
            completed=Count("id", filter=Q(status="COMPLETED")),
            in_progress=Count("id", filter=Q(status="IN_PROGRESS")),
            pending=Count("id", filter=Q(status="PENDING")),
        )
        return context

@user_passes_test(is_employee)
def employee_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

#Todo should convert cbv employee dashboard 

class EmployeeDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    login_url = "sign-in"
    template_name = "dashboard/user-dashboard.html"

    def test_func(self):
        return is_employee(self.request)

create_decorators = [
    login_required,
    permission_required("tasks.add_task", login_url='no-permission')
]

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
        task = task_form.save(commit=False) 
        project_id = request.POST.get("project") 
        try:
            task.project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            messages.error(request, "Invalid project selected.")
            return self.get(request, *args, **kwargs)

        task.save()

        task_detail = task_detail_form.save(commit=False)
        task_detail.task = task
        task_detail.save()

        messages.success(request, "Task Created Successfully")
        return redirect("create-task")

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
class TaskListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = "no-permission"
    permission_required = "tasks.view_task"
    model = Task
    template_name = "show_task.html"
    context_object_name = "tasks" 

    def get_queryset(self):
        queryset = Task.objects.prefetch_related("assigned_to").all()
        print("tasks =", queryset)

        # Retrieve task with "paper" in the title
        tasks1 = queryset.filter(title__icontains="paper")

        # Retrieve tasks containing 'c' and status is 'PENDING'
        tasks2 = queryset.filter(title__icontains="c", status="PENDING")

        # Retrieve tasks that are PENDING or IN_PROGRESS
        tasks3 = queryset.filter(Q(status="PENDING") | Q(status="IN_PROGRESS"))

        # Check if a task with an invalid status exists
        tasks4 = queryset.filter(status="adfsdskfd").exists()

        for task in queryset:
            print(task.assigned_to.all())

        return queryset 

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        queryset = Task.objects.prefetch_related("assigned_to").all()

        context["tasks1"] = queryset.filter(title__icontains="paper")
        context["tasks2"] = queryset.filter(title__icontains="c", status="PENDING")
        context["tasks3"] = queryset.filter(Q(status="PENDING") | Q(status="IN_PROGRESS"))
        context["tasks4"] = queryset.filter(status="adfsdskfd").exists()
        
        return context

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


#Todo should convert cbv delete task 
class TaskDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    login_url = "sign-in"
    permission_required = "tasks.delete_task"
    model = Task
    success_url = reverse_lazy("manager-dashboard")

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        if task:
            messages.success(self.request, "Task Deleted Successfully")
            return super().post(request, *args, **kwargs)
        else:
            messages.error(self.request, "Something went wrong")
            return redirect("manager-dashboard")


@login_required
def dashboard(request):
  if is_admin(request.user):
    return redirect('admin-dashboard')
  elif is_manager(request.user):
    return redirect('manager-dashboard')
  elif is_employee(request.user):
    return redirect('user-dashboard')
  return redirect('no-permission')

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