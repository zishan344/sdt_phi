from django.shortcuts import render, redirect
from users.forms import RegisterForm,CustomRegistrationForm
from django.contrib.auth.models import User,Group
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from users.forms import LoginForm
from django.contrib.auth.tokens import default_token_generator
from users.forms import LoginForm, AssignRoleForm, CreateGroupForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.db.models import Prefetch
from django.contrib.auth.views import LoginView,TemplateView

def is_manager(user):
  return user.groups.filter(name='Manager').exists()

def is_employee(user):
  return user.groups.filter(name='Employee').exists()
def is_admin(user):
  return user.groups.filter(name='Admin').exists()

def activate_user(request,user_id, token):
  try:
    user = User.objects.get(id = user_id)
    if default_token_generator.check_token(user, token):
      user.is_active = True
      user.save()
      return redirect('sign-in')
    else:
      return HttpResponse('Invalid Id or token')
  except User.DoesNotExist:
      return HttpResponse('User not found')

def sign_up(request):
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
          user = form.save(commit=False)
          user.set_password(form.cleaned_data.get('password1'))
          user.is_active = False
          user.save()
          messages.success(request,'A Confirmation mail send. Please Check your email')
          return redirect('sign-in')
        else:
          print("Form is not valid")
    else:
        form = CustomRegistrationForm()

    return render(request, 'registration/register.html', {"form": form})

def sign_in (request):
  form = LoginForm()
  if request.method == 'POST':
    form = LoginForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request,user)
      return redirect('home')
  return render(request,'registration/login.html',{'form':form})

class CustomLoginForm(LoginView):
  form_class = LoginForm
  def get_success_url(self):
    next_url = self.request.GET.get('next')
    return next_url if next_url else super().get_success_url()

class ProfileView(TemplateView):
  template_name = 'accounts/profile.html'
  def get_context_data(self,**kwargs):
    context = super().get_context_data(**kwargs)
    user = self.request.user
    context['username'] = user.username
    context['email'] = user.email
    context['name'] = user.get_full_name()
    context['member_since'] = user.date_joined
    context['last_login'] = user.last_login
    return context

@login_required
def sign_out(request):
  if request.method == 'POST':
    logout(request)
    return redirect('sign-in')
  
@user_passes_test(is_admin,login_url='no-permission')
def admin_dashboard(request):
  users = User.objects.prefetch_related(
    Prefetch('groups',queryset=Group.objects.all(),to_attr='all_groups')
  ).all()
  for user in users:
    if user.all_groups:
      user.group_name = user.all_groups[0].name
    else:
      user.group_name = 'No Group Assigned'
  return render(request, 'admin/dashboard.html',{"users":users})

@user_passes_test(is_admin,login_url='no-permission')
def assign_role(request,user_id):
  user = User.objects.get(id = user_id)
  form = AssignRoleForm()
  if request.method == 'POST':
    form = AssignRoleForm(request.POST)
    if form.is_valid():
      role = form.cleaned_data.get('role')
      user.groups.clear() # remove old roles
      user.groups.add(role)
      messages.success(request,f"User {user.username} has been assigned to {role.name} role")
      return redirect('admin-dashboard')
  return render(request,'admin/assign_role.html',{'form':form})
@user_passes_test(is_admin,login_url='no-permission')
def create_group(request):
  form = CreateGroupForm()
  if request.method == 'POST':
    form = CreateGroupForm(request.POST)
    
    if form.is_valid():
      group = form.save()
      messages.success(request, f"Group {group.name} has been created successfully")
      return redirect('create-group')
  return render(request, 'admin/create_group.html', {'form': form})

@user_passes_test(is_admin,login_url='no-permission')
def group_list(request):
  groups = Group.objects.prefetch_related('permissions').all()
  return render(request, 'admin/group_list.html',{'groups':groups})
