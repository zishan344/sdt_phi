from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
import re
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
  class Meta:
    model = User
    fields =['username', 'first_name','last_name', 'password1', 'password2', 'email']
  def __init__(self, *args, **kwargs):
    super(UserCreationForm, self).__init__(*args, **kwargs)
    for fieldname in ['username', 'password1', 'password2']:
      self.fields[fieldname].help_text = None
  

class CustomRegistrationForm(forms.ModelForm):
  class Meta:
    fields = [
      'username','first_name','last_name','password1','confirm_password','email'
    ]
  def clean_password1(self):
    password1 = self.cleaned_data.get('password1')
    # check for minimum length
    if len(password1) < 8:
      raise forms.ValidationError(
        "Password must be at least 8 characters long"
      )
    # check for complexity (uppercase, lowercase, number, special characters)
    elif not re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}",password1):
      raise forms.ValidationError(
        'Password must include uppercase, lowercase,number, and special character'
      )
    return password1

