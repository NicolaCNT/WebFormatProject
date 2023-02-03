from django.shortcuts import render, redirect
from .forms import CreateTaskForm, AssignTaskToDevForm
from .models import *
from django.views import View

# Create your views here.

class Dashboard(View):

    def get(self, request):
        all_tasks_assigned = TaskAssigned.objects.order_by("developer").all()
        context={"all_tasks_assigned": all_tasks_assigned}
        return render(request, "dashboard.html", context)

class TaskCreate(View):

    def get(self, request):
        all_project_managers = Employee.objects.filter(role='PM')
        context = {'project_managers': all_project_managers}
        return render(request, "createTask.html", context)

    def post(self, request):
        create_task_form = CreateTaskForm(request.POST)
        if create_task_form.is_valid():
            create_task_form.save()
            return redirect('dashboard')

class TaskAssign(View):
    def get(self, request):
        devs = Employee.objects.filter(role = 'DEV')
        tasks_to_assign = Task.objects.filter(status='waiting') or Task.objects.filter(status='processing')
        context = {'tasks_to_assign' : tasks_to_assign,
                   'devs': devs}
        return render(request, "assignTask.html", context)
    def post(self, request):
        assign_task_form = AssignTaskToDevForm(request.POST)
        task_fk = request.POST['task']
        task = Task.objects.get(id=task_fk)
        if task.status == 'waiting':
            task.status = 'processing'
            task.save()
        if assign_task_form.is_valid():
            assign_task_form.save()
            return redirect('dashboard')
        

class TaskRemove(View):
    
    def get(self, request, pk):
        id_task_to_remove = TaskAssigned.objects.get(id=pk)
        context = {'task_to_remove': id_task_to_remove}
        return render(request, "remove_task.html", context)
    
    def post(self, request, pk):
        id_task_to_remove = TaskAssigned.objects.get(id=pk)
        id_task_to_remove.delete()
        return redirect("dashboard")
