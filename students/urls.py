"""
URL configuration for schoolsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee_form/', views.employee_form, name='employee_form'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('show/', views.show, name='show'),
    path('<int:id>/', views.employee_list, name='employee_update'),
    path('delete/<int:id>', views.delete, name='delete'),

]
