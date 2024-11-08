from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('student_signup/', views.student_signup, name='student_signup'),
    path('ta_signup/', views.ta_signup, name='ta_signup'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('ta_dashboard/', views.ta_dashboard, name='ta_dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]