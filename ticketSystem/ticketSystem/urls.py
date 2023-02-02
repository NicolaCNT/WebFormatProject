from django.contrib import admin
from django.urls import path
from ticketApp import views

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
    path('create_task/', views.TaskCreate.as_view(), name="create_task"),
    path('assign_task/', views.TaskAssign.as_view(), name="assign_task"),
    path('admin/', admin.site.urls),
]
