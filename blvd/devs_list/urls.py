from django.urls import path
from . import views

urlpatterns = [
    path('', views.developer_list, name='devs_list'),
]