from django.urls import path
from . import views

urlpatterns = [
    path('employees', views.Employeelistview, name='home'),
    path('employees/<int:pk>', views.employeeDetailview, name='home'),
    path('Userlistview/', views.Userlistview, name='home'),
    

]