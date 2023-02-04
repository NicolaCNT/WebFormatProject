from django.contrib import admin
from django.urls import path
from ticketApp import views

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
    path('create_task/', views.TaskCreate.as_view(), name="create_task"),
    path('assign_task/<int:pk>/', views.TaskAssign.as_view(), name="assign_task"),
    path('remove_task/<int:pk>/', views.TaskRemove.as_view(), name="remove_task"),
    path('processing_task/<int:pk>/', views.TaskProcessing.as_view(), name="processing_task"),
    path('admin/', admin.site.urls),
]
