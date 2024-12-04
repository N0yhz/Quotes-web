from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetConfirmView ,PasswordResetDoneView, PasswordResetCompleteView

app_name = 'users'
urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register'),
    path('profile/', views.profile, name='profile'),
    path('reset-password/', views.ResetPasswordView.as_view(), name = 'password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name = 'users/password_reset_done.html'), name = 'password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name = 'password-reset-complete'),
]
