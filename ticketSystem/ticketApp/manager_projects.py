from .models import Project
from .manager_employees import ManagerEmployees


class ManagerProjects():
    projects = Project.objects.all()
    employees = ManagerEmployees()
    project_managers = employees.get_employees_by_role('PM')

    def get_all(self):
        return self.projects
    
    def get_project(self, pk):
        project = self.projects.get(id=pk)
        return project
    
    def get_cross_team_projects(self):
        projects = self.projects
        cross_team_projects = []

        for project in projects:
            if project.assigned_to.count() > 1:
                cross_team_projects.append(project)
        
        return cross_team_projects
    
    def get_project_managers_already_assigned(self, project_pk):
        project = self.get_project(project_pk)
        project_managers_already_assigned = project.assigned_to.all()
        return project_managers_already_assigned
    
    def get_project_managers_unassigned(self, project_pk):
        project_managers_unassigned = self.project_managers.exclude(pk__in=self.get_project_managers_already_assigned(project_pk))
        return project_managers_unassigned
    
    def assign_projects_to(self, project_pk, project_manager_pk):
        project = self.get_project(project_pk)
        project_manager = self.employees.get_employee(project_manager_pk)
        project.assigned_to.add(project_manager)