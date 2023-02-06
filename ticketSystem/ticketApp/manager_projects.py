from .models import Project, Employee
from .manager_employees import ManagerEmployees
from django.db.models import QuerySet

class ManagerProjects():
    projects = Project.objects.all()
    employees = ManagerEmployees()
    project_managers = employees.get_employees_by_role('PM')
    
    def get_project(self, pk : int) -> Project:

        """Function that returns a specific project matching with the primary key passed by argument
        Args:
            pk (int): primary key of a project object
        Returns:
            Project: Object matching with the primary key
        """

        project = self.projects.get(id=pk)
        return project
    
    def get_cross_team_projects(self) -> QuerySet[Project]:

        """Function that returns the projects under developement by multiple teams

        Returns:
            QuerySet[Project]: QuerySet composed by projects 
        """

        projects = self.projects
        cross_team_projects = []

        for project in projects:
            if project.assigned_to.count() > 1:
                cross_team_projects.append(project)
        
        return cross_team_projects
    
    def get_project_managers_already_assigned(self, project_pk : int) -> QuerySet[Employee]:
        """Function that returns project manager working to a project given the project's primary key

        Args:
            project_pk (int): primary key of the project

        Returns:
            QuerySet[Employee]: QuerySet of project managers working on a project
        """

        project = self.get_project(project_pk)
        project_managers_already_assigned = project.assigned_to.all()
        return project_managers_already_assigned
    
    def get_project_managers_unassigned(self, project_pk : int) -> QuerySet[Employee]:
        """Function that returns project manager not assigned to a project given the project's primary key
        Args:
            project_pk (int): primary key of the project
        Returns:
            QuerySet[Employee]: QuerySet of project managers not working on a project
        """
        project_managers_unassigned = self.project_managers.exclude(pk__in=self.get_project_managers_already_assigned(project_pk))
        return project_managers_unassigned
    
    def assign_project_to(self, project_pk : int, project_manager_pk : int):
        """Function that assigns a project to a project manager given their primary keys
        Args:
            project_pk (int): primary key of the project
            project_manager_pk (int): primary key of the project manager
        """
        project = self.get_project(project_pk)
        project_manager = self.employees.get_employee(project_manager_pk)
        project.assigned_to.add(project_manager)