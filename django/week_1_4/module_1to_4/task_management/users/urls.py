from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from users.views import sign_up,sign_in,sign_out,activate_user,admin_dashboard,assign_role,create_group,group_list,CustomLoginForm,ProfileView,ChangePassword, CustomPasswordResetView,CustomPasswordResetConfirmView

urlpatterns = [
    path("sign-up/", sign_up, name="sign-up"),
    # path("sign-in/", sign_in, name="sign-in"),
    path("sign-in/", CustomLoginForm.as_view(), name="sign-in"),
    # path("sign-out/", sign_out, name="sign-out"),
    path("sign-out/", LogoutView.as_view(), name="sign-out"),
    path('activate/<int:user_id>/<str:token>/', activate_user),
    path('admin/dashboard/',admin_dashboard, name="admin-dashboard"),
    path('admin/<int:user_id>/assign-role/',assign_role,name='assign-role'),
    path('admin/create-group/',create_group,name='create-group'),
    path('admin/group-list/',group_list, name='group-list'),
    path("profile/", ProfileView.as_view(), name=""),
    path("password-change/", ChangePassword.as_view(), name="password-change"),
    path("password-change/done/", PasswordChangeDoneView.as_view(template_name="accounts/password_change_done.html"), name="password_change_done"),
    path("password-reset/", CustomPasswordResetView.as_view(), name="password_reset"),
    path("password-reset/confirm/<uidb64>/<token>/", CustomPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]
