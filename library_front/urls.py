from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('get', views.get, name = 'get'),
    path('get_all', views.get_all, name = 'get_all'),
    path('add_book', views.add_book, name = 'add_book'),
    path('put_data_complete', views.put_data_complete, name = 'put_data_complete'),
    path('delete', views.delete_data, name = 'delete'),
    path('register', views.register, name = 'register'),
    path('login', views.login_view, name = 'login'),
    path('validate_name', views.validate_name, name = 'validate_name'),
    path('logout', views.logout_view, name = 'logout')
    
]
