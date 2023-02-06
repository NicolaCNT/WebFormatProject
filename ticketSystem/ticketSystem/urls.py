from django.contrib import admin
from django.urls import path
from ticketApp import views

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
    path('create-task/', views.TaskCreate.as_view(), name="create_task"),
    path('assign-task/<int:pk>/', views.TaskAssign.as_view(), name="assign_task"),
    path('remove-task/<int:pk>/', views.TaskRemove.as_view(), name="remove_task"),
    path('processing-task/<int:pk>/', views.TaskProcessing.as_view(), name="processing_task"),
    path('assign-project/<int:pk>/', views.ProjectAssign.as_view(), name="assign_project"),
    path('cross-team-projects/', views.ProjectsCrossTeam.as_view(), name="cross_team_projects"),
    path('admin/', admin.site.urls),
]
