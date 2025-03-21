from django.shortcuts import render, redirect,get_object_or_404
from users.forms import RegisterForm,CustomRegistrationForm,CustomPasswordChangeForm,CustomPasswordResetForm, CustomPasswordResetConfirmForm, EditProfileForm
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from users.forms import LoginForm
from django.contrib.auth.tokens import default_token_generator
from users.forms import LoginForm, AssignRoleForm, CreateGroupForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.db.models import Prefetch
from django.contrib.auth.views import LoginView,TemplateView,PasswordChangeView,PasswordResetView, PasswordResetConfirmView
from django.views.generic import UpdateView, CreateView, View, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic.edit import FormView


from django.contrib.auth import get_user_model

User = get_user_model()


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


#* starting view functions and classes
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

class ChangePassword(PasswordChangeView):
  template_name = "accounts/password_change.html"
  form_class = CustomPasswordChangeForm

class CustomPasswordResetView(PasswordResetView):
  form_class = CustomPasswordResetForm
  template_name = 'registration/reset_password.html'
  success_url = reverse_lazy('sign-in')
  html_email_template_name = 'registration/reset_email.html'
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['protocol']='https'if self.request.is_secure() else 'http'
    context['domain'] = self.request.get_host()
    print(context)
    return context
  def form_valid(self,form):
    messages.success(
      self.request, 'A Reset email set. Please check your email inbox or spam folder'
    )
    return super().form_valid(form)

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
  form_class = CustomPasswordResetConfirmForm
  template_name = 'registration/reset_password.html'
  success_url = reverse_lazy('sign-in')
  def form_valid(self,form):
    messages.success(
      self.request, 'Password reset successfully'
    )
    return super().form_valid(form)

class ProfileView(TemplateView):
  template_name = 'accounts/profile.html'
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user = self.request.user
    context['username'] = user.username
    context['email'] = user.email
    context['name'] = user.get_full_name()
    context['bio'] = user.bio
    context['profile_image'] = user.profile_image

    context['member_since'] = user.date_joined
    context['last_login'] = user.last_login
    return context

class EditProfileView(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'accounts/update_profile.html'
    context_object_name = 'form'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return redirect('profile')

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

#Todo should convert cbv assign role 
class AssignRole(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    login_url = 'sign-in'
    permission_required = "auth.change_group"
    form_class = AssignRoleForm
    template_name = 'admin/assign_role.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = get_object_or_404(User, id=self.kwargs['user_id'])  # Fetch user
        role = form.cleaned_data.get('role')
        user.groups.clear()  # Remove old roles
        user.groups.add(role)  # Assign new role
        messages.success(self.request, f"User {user.username} has been assigned to {role.name} role")
        return super().form_valid(form)

#Todo should convert cbv create group
class CreateGroup(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
  login_url = 'sign-in'
  permission_required ="auth.add_group"
  model = Group
  form_class = CreateGroupForm
  template_name ='admin/create_group.html'
  success_url = reverse_lazy('create-group')
  def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "New Group created successfully")
        return response


#Todo should convert cbv group list
class GroupListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    login_url = 'no-permission'
    permission_required = "auth.view_group"
    model = Group
    template_name = 'admin/group_list.html'
    context_object_name = 'groups'