from django.urls import path
from tasks.views import manager_dashboard, employee_dashboard, create_task,view_task,update_task, delete_task, dashboard,task_details,MyView,GreetingView,MorningGreetingView,CreateTask,ViewProject,TakDetails,UpdateTask
urlpatterns = [
  path('manager-dashboard/', manager_dashboard,name="manager-dashboard"),
  path('user-dashboard/', employee_dashboard),
  # path('create-task/', create_task,name="create-task"),
  path('create-task/', CreateTask.as_view(),name="create-task"),
  path('view-allTask/', view_task),
  # path('update-task/<int:id>/',update_task,name="update-task"),
  path('update-task/<int:id>/',UpdateTask.as_view(),name="update-task"),
  path('delete-task/<int:id>/',delete_task,name="delete-task"),
  path('dashboard/', dashboard, name='dashboard'),
  # path("task-details/<int:task_id>/",task_details, name="task-details"),
  path("task-details/<int:task_id>/",TakDetails.as_view(),name="task-details"),
  path("about/", MyView.as_view(), name="about"),
  path("greeting/", GreetingView.as_view(greeting="Hello there!"), name="greeting"),
  path("morning-greeting/", MorningGreetingView.as_view()),
  path("view_project/",ViewProject.as_view())
]