from django.db import models

# Create your models here.

class Employee(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)


class Task(models.Model):
  project = models.ForeignKey("Project", on_delete = models.CASCADE,default=1)
  assigned_to = models.ManyToManyField(Employee)
  # newString = models.models.CharField( max_length=250,default='' )
  title = models.CharField(max_length=250)
  description = models.TextField()
  due_date = models.DateField()
  is_complete = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class TaskDetail(models.Model):
  HIGH ='H'
  MEDIUM ='M'
  LOW ='L'
  PRIORITY_CHOICES = (
    (HIGH,'High'),
    (MEDIUM,'Medium'),
    (LOW,'Low'),
  )
  task = models.OneToOneField(Task,on_delete=models.CASCADE,related_name='details')
  assigned_to = models.CharField(max_length=100)
  priority = models.CharField(
    max_length = 1, choices =PRIORITY_CHOICES, default = LOW
    )
  # notes = models.models.TextField(blank=True, null=True)

class Project(models.Model):
  name = models.CharField(max_length = 100)
  start_date = models.DateField()