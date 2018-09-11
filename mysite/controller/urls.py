from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name = "register"),
    path('changePwd', views.changePwd, name = "changePwd"),
    path('send_image/', views.send_image),
]