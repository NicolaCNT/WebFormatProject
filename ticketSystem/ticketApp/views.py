from django.shortcuts import render, redirect
from .forms import CreateTaskForm, AssignTaskToDevForm
from .models import *
from django.db.models import Q
from django.views import View

# Create your views here.

class Dashboard(View):

    def get(self, request):
        developers = Employee.objects.filter(role = 'DEV')
        #all_tasks_assigned = TaskAssigned.objects.order_by("developer").all()
        for dev in developers:
            developer = Employee.objects.get(name_employee = dev.name_employee)
            tasks_assigned = developer.devs.filter( status = 'processing' )
        tasks_to_assign = Task.objects.filter(Q(status = 'processing') | Q(status = 'waiting'))
        context={
            #"all_tasks_assigned": all_tasks_assigned,
            "tasks_to_assign": tasks_to_assign,
            "tasks" : tasks_assigned,
            "developers": developers}
        return render(request, "dashboard.html", context)


class TaskCreate(View):

    def get(self, request):
        all_project_managers = Employee.objects.filter(role='PM')
        context = {'project_managers': all_project_managers}
        return render(request, "create_task.html", context)

    def post(self, request):
        create_task_form = CreateTaskForm(request.POST)
        if create_task_form.is_valid():
            create_task_form.save()
            return redirect('dashboard')

class TaskAssign(View):
    def get(self, request, pk):
        task_to_assign = Task.objects.get(id=pk)
        all_devs = Employee.objects.filter(role = 'DEV')
        devs_to_assign = []
        for dev in all_devs:
            if dev.id != task_to_assign.assigned_to:
                devs_to_assign.append(dev)
        
        context = {'task_to_assign' : task_to_assign,
                   'devs' : devs_to_assign,
                   }
        return render(request, "assign_task.html", context)
    
    def post(self, request):

        assign_task_form = AssignTaskToDevForm(request.POST)
        dev = Employee.objects.get(id=dev_pk)
        task_to_assign = Task.objects.get(id=task_pk)
        if assign_task_form.is_valid():
            task_to_assign.devs.add(dev)
            assign_task_form.save()
            return redirect('dashboard')
        

class TaskRemove(View):
    
    def get(self, request, pk):
        task_to_remove = Task.objects.get(id=pk)
        context = {'task_to_remove': task_to_remove}
        return render(request, "remove_task.html", context)
    
    def post(self, request, pk):
        task_to_remove = Task.objects.get(id=pk)
        task_to_remove.delete()
        return redirect("dashboard")

class TaskProcessing(View):
    def get(self, request, pk):
        dev = Employee.objects.get(id=pk)
        developer_tasks = Task.objects.filter(assigned_to=dev.id, status = 'processing')
        

        context = {'dev' : dev, 'developer_tasks': developer_tasks}
        return render(request, "processing_task.html", context)

    def post(self, request, pk):
        #developer_tasks = TaskAssigned.objects.filter(developer = pk).values("task")
        #tasks_processing = developer_tasks.filter(status = "processing")
        #context = {'tasks_processing': tasks_processing}
        pass