from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('success', views.success, name='success')
]