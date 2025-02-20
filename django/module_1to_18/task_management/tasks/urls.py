from django.urls import path
from tasks.views import TaskDeleteView, dashboard,MyView,GreetingView,MorningGreetingView,CreateTask,ViewProject,TakDetails,UpdateTask,ManagerDashboardView,EmployeeDashboardView,TaskListView,manager_dashboard,create_task
urlpatterns = [
  # path('manager-dashboard/', ManagerDashboardView.as_view(),name="manager-dashboard"),
  path('manager-dashboard/', manager_dashboard,name="manager-dashboard"),
  path('user-dashboard/', EmployeeDashboardView.as_view()),
  path('create-task/', CreateTask.as_view(),name="create-task"),
  path('view-allTask/', TaskListView.as_view()),
  path('update-task/<int:id>/',UpdateTask.as_view(),name="update-task"),
  path('delete-task/<int:id>/',TaskDeleteView.as_view(),name="delete-task"),
  path('dashboard/', dashboard, name='dashboard'),
  path("task-details/<int:task_id>/",TakDetails.as_view(),name="task-details"),
  path("about/", MyView.as_view(), name="about"),
  path("greeting/", GreetingView.as_view(greeting="Hello there!"), name="greeting"),
  path("morning-greeting/", MorningGreetingView.as_view()),
  path("view_project/",ViewProject.as_view())
]