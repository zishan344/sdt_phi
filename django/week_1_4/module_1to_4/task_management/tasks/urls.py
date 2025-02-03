from django.urls import path
from tasks.views import manager_dashboard, employee_dashboard, test, create_task,view_task,update_task, delete_task, dashboard,task_details
urlpatterns = [
  path('manager-dashboard/', manager_dashboard,name="manager-dashboard"),
  path('user-dashboard/', employee_dashboard),
  path('test/', test),
  path('create-task/', create_task,name="create-task"),
  path('view-allTask/', view_task),
  path('update-task/<int:id>/',update_task,name="update-task"),
  path('delete-task/<int:id>/',delete_task,name="delete-task"),
  path('dashboard', dashboard, name='dashboard'),
  path("task/<int:task_id>/details/",task_details, name="task_details")
]