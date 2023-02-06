from .models import Employee, Task
from .manager_tasks import ManagerTasks
from django.db.models import QuerySet

class ManagerEmployees():
    employees = Employee.objects.all()
    tasks = ManagerTasks()

    def get_employees_by_role(self, role_to_filter : str) -> QuerySet[Employee]:

        """Function that returns all the employees with a specific role
        Args:
            role_to_filter (str): role that has to be filtered
        Returns:
            QuerySet[Employee]: QuerySet composed by employee objects
        """

        employees_with_role = self.employees.filter(role = role_to_filter)
        return employees_with_role
    
    def get_employee(self, pk : int) -> Employee:

        """Function that returns the employee matching with a primary key
        Args:
            pk (int): primary key of an employee
        Returns:
            Employee: Matching with the primary key
        """

        employee = self.employees.get(id=pk)
        return employee
    
    def get_developer_tasks_processing(self, developer_pk : int) -> QuerySet[Task]:
        """Function that returns the tasks in processing by a developer
        Args:
            employee_pk (int): primary key of a developer
        Returns:
            QuerySet[Task]: QuerySet of tasks in processing by the developer matching with the primary key and in processing status
        """
        developer = self.get_employee(developer_pk)
        developer_tasks_processing = self.tasks.get_tasks_processing_by_developer(developer)
        return developer_tasks_processing
    
    def get_devs_already_assigned_to_task(self, task_pk : int) -> QuerySet[Employee]:
        """Function that returns developers already assigned to a specific task
        Args:
            task_pk (int): Primary key of a task
        Returns:
            QuerySet[Employee]: QuerySet of employees assigned to the task matching with the primary key
        """
        task = self.tasks.get_task(task_pk)
        devs_already_assigned = task.assigned_to.all()
        return devs_already_assigned
    
    def get_devs_unassigned_to_task(self, task_pk : int) -> QuerySet[Employee]:
        """Function that returns developers unassigned to a specific task
        Args:
            task_pk (int): Primary key of a task
        Returns:
            QuerySet[Employee]: QuerySet of employees not assigned to the task matching
        """
        developers = self.get_employees_by_role('DEV')
        devs_unassigned = developers.exclude(pk__in=self.get_devs_already_assigned_to_task(task_pk))
        return devs_unassigned
    
    
