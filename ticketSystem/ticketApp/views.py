from django.shortcuts import render, redirect
from .forms import CreateTaskForm
from .manager_employees import ManagerEmployees
from .manager_projects import ManagerProjects
from .manager_tasks import ManagerTasks
from .models import *
from django.views import View

# Create your views here.

class Dashboard(View):

    manager_employees = ManagerEmployees()
    manager_projects = ManagerProjects()
    manager_tasks = ManagerTasks()


    def get(self, request):
        
        developers = self.manager_employees.get_employees_by_role('DEV')
        projects = self.manager_projects.projects
        tasks_to_assign = self.manager_tasks.get_assignable_tasks()

        context={
            "projects": projects,
            "tasks_to_assign": tasks_to_assign,
            "developers": developers}
        return render(request, "dashboard.html", context)


class TaskCreate(View):

    def get(self, request):
        manager_employees = ManagerEmployees()
        project_managers = manager_employees.get_employees_by_role('PM')
        context = {'project_managers': project_managers}
        return render(request, "create_task.html", context)

    def post(self, request):
        create_task_form = CreateTaskForm(request.POST)
        if create_task_form.is_valid():
            create_task_form.save()
            return redirect('dashboard')

class TaskAssign(View):
    manager_employees = ManagerEmployees()
    manager_tasks = ManagerTasks()
    def get(self, request, pk):
        task_to_assign = self.manager_tasks.get_task(pk)
        devs_to_assign = self.manager_employees.get_devs_unassigned_to_task(pk)
        
        context = {'task_to_assign' : task_to_assign,
                   'devs' : devs_to_assign,
                   }
        return render(request, "assign_task.html", context)
    
    def post(self, request, **kwargs):
        task_pk = kwargs["pk"]
        dev_pk = request.POST.get('dev_pk')
        try:
            developer = self.manager_employees.get_employee(dev_pk)
            task_to_assign = self.manager_tasks.get_task(task_pk)
            task_to_assign.assigned_to.add(developer)
            if task_to_assign.get_status() == 'waiting':
                task_to_assign.set_status('processing')
            task_to_assign.save()
            return redirect('dashboard')
        except Employee.DoesNotExist as employee_error:
            return render(request, 'error.html', {'error': employee_error})
        

class TaskRemove(View):
    manager_tasks = ManagerTasks()
    def get(self, request, pk):
        task_to_remove = self.manager_tasks.get_task(pk)
        context = {'task_to_remove': task_to_remove}
        return render(request, "remove_task.html", context)
    
    def post(self, request, pk):
        task_to_remove = self.manager_tasks.get_task(pk)
        task_to_remove.delete()
        return redirect("dashboard")


class TaskProcessing(View):

    manager_employees = ManagerEmployees()
    manager_tasks = ManagerTasks()

    def get(self, request, pk):
        developer = self.manager_employees.get_employee(pk)
        developer_tasks = self.manager_employees.get_developer_tasks_processing(pk)
        context = {'dev' : developer, 'developer_tasks': developer_tasks}
        return render(request, "processing_task.html", context)


class ProjectAssign(View):

    manager_employees = ManagerEmployees()
    manager_projects = ManagerProjects()


    def get(self, request, pk):
        project_to_assign = self.manager_projects.get_project(pk)
        project_managers_unassigned = self.manager_projects.get_project_managers_unassigned(pk)
        context = {
            'project_managers' : project_managers_unassigned,
            'project': project_to_assign
            }
        return render(request, "assign_project.html", context)
    
    def post(self, request, **kwargs):
        project_pk = kwargs["pk"]
        project_manager_pk = request.POST.get('pm_pk')
        try:
            self.manager_projects.assign_project_to(project_pk, project_manager_pk)
            return redirect('dashboard')
        except Employee.DoesNotExist as employee_error:
            return render(request, 'error.html', {'error': employee_error})
        
    
class ProjectsCrossTeam(View):

    manager_projects = ManagerProjects()

    def get(self, request):
        cross_team_projects = self.manager_projects.get_cross_team_projects()
        context = {'cross_team_projects': cross_team_projects}
        return render(request, "cross_team_projects.html", context)

        

    