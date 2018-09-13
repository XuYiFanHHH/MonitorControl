from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name = "register"),
    path('changePwd', views.changePwd, name = "changePwd"),
    path('send_image/', views.send_image),

    path('get_onepage_warnings', views.get_onepage_warnings, name = "get_onepage_warnings"),
    path('delete_warning', views.delete_warning, name = "delete_warning"),
    path('add_warning', views.add_warning, name = "add_warning"),
]