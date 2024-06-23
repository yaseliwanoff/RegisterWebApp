from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomePage, name='home'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('', views.SignUpPage, name='signup'),
]
