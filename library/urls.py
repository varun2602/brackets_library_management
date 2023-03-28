from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('get_book', views.get_book, name = 'get_book'),
    path('add_book', views.add_book, name = 'add_book'),
    path('put_data_complete', views.put_data_complete, name = 'put_data_complete'),
    path('put_data_partial', views.put_data_partial, name = 'put_data_partial'),
    path('delete_data', views.delete_data, name = 'delete_data')
]