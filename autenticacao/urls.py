from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registo_curso/', views.registo_curso_view, name="registo_curso"),
    path('login_curso/', views.login_curso_view, name="login_curso"),
    path('logout_curso/', views.logout_curso_view, name="logout_curso"),

    # recuperação de password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='registration/custom_password_reset_form.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/custom_password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/custom_password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/custom_password_reset_complete.html'), name='password_reset_complete'),
]