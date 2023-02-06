from django.shortcuts import render, redirect
from .forms import CreateTaskForm, AssignTaskToDevForm
from .manager_employees import ManagerEmployees
from .manager_projects import ManagerProjects
from .manager_tasks import ManagerTasks
from .models import *
from django.db.models import Q
from django.views import View

# Create your views here.

class Dashboard(View):

    employees = ManagerEmployees()
    projects = ManagerProjects()
    tasks = ManagerTasks()


    def get(self, request):
        
        developers = self.employees.get_employees_by_role('DEV')
        projects = self.projects.get_all()
        tasks_to_assign = self.tasks.get_assignable_tasks()

        context={
            "projects": projects,
            "tasks_to_assign": tasks_to_assign,
            "developers": developers}
        return render(request, "dashboard.html", context)


class TaskCreate(View):

    def get(self, request):
        employees = ManagerEmployees()
        project_managers = employees.get_employees_by_role('PM')
        context = {'project_managers': project_managers}
        return render(request, "create_task.html", context)

    def post(self, request):
        create_task_form = CreateTaskForm(request.POST)
        if create_task_form.is_valid():
            create_task_form.save()
            return redirect('dashboard')

class TaskAssign(View):
    def get(self, request, pk):
        tasks = ManagerTasks()
        employees = ManagerEmployees()
        task_to_assign = tasks.get_task()
        developers = employees.get_employees_by_role('DEV')
        devs_to_assign = []
        for dev in developers:
            if dev.id != task_to_assign.assigned_to:
                devs_to_assign.append(dev)
        
        context = {'task_to_assign' : task_to_assign,
                   'devs' : devs_to_assign,
                   }
        return render(request, "assign_task.html", context)
    
    def post(self, request, dev_pk, task_pk):

        assign_task_form = AssignTaskToDevForm(request.POST)
        dev = Employee.objects.get(id=dev_pk)
        task_to_assign = Task.objects.get(id=task_pk)
        if assign_task_form.is_valid():
            task_to_assign.devs.add(dev)
            assign_task_form.save()
            return redirect('dashboard')
        

class TaskRemove(View):
    tasks = ManagerTasks()
    def get(self, request, pk):
        task_to_remove = self.tasks.get_task(pk)
        context = {'task_to_remove': task_to_remove}
        return render(request, "remove_task.html", context)
    
    def post(self, request, pk):
        task_to_remove = self.tasks.get_task(pk)
        task_to_remove.delete()
        return redirect("dashboard")


class TaskProcessing(View):
    employees = ManagerEmployees()
    def get(self, request, pk):
        developer = self.employees.get_employee(pk)
        developer_tasks = self.employees.get_developer_tasks_processing(pk)
        context = {'dev' : developer, 'developer_tasks': developer_tasks}
        return render(request, "processing_task.html", context)

    def post(self, request):
        #developer_tasks = TaskAssigned.objects.filter(developer = pk).values("task")
        #tasks_processing = developer_tasks.filter(status = "processing")
        #context = {'tasks_processing': tasks_processing}
        pass

class ProjectAssign(View):

    employees = ManagerEmployees()
    projects = ManagerProjects()


    def get(self, request, pk):
        project_to_assign = self.projects.get_project(pk)
        project_managers_unassigned = self.projects.get_project_managers_unassigned(pk)
        context = {
            'project_managers' : project_managers_unassigned,
            'project': project_to_assign
            }
        return render(request, "assign_project.html", context)
    
    def post(self, request, **kwargs):
        project_pk = kwargs["pk"]
        project_manager_pk = request.POST.get('pm_pk')
        self.projects.assign_projects_to(project_pk, project_manager_pk)
        return redirect('dashboard')
    
class ProjectsCrossTeam(View):

    projects = ManagerProjects()

    def get(self, request):
        cross_team_projects = self.projects.get_cross_team_projects()
        context = {'cross_team_projects': cross_team_projects}
        return render(request, "cross_team_projects.html", context)

        

    