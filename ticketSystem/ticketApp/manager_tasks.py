from .models import Task, Employee
from django.db.models import Q
from django.db.models import QuerySet


class ManagerTasks():
    tasks = Task.objects.all()

    def get_task(self, pk : int) -> Task:
        """Function that returns the task matching given his primary key
        Args:
            pk (int): primary key of the task
        Returns:
            Task: Object that matches with the primary key
        """
        task = self.tasks.get(id=pk)
        return task

    def get_assignable_tasks(self) -> QuerySet[Task]:
        """Function that returns all the tasks that can be assigned
        Returns:
            QuerySet[Task]: QuerySet composed by assignable tasks
        """
        assignable_tasks = self.tasks.filter(Q(status = 'processing') | Q(status = 'waiting'))
        return assignable_tasks
    
    def get_tasks_processing_by_developer(self, developer : Employee) -> QuerySet[Task]:
        """Function that returns tasks being processed by a developer given by argument
        Args:
            developer (Employee): developer 
        Returns:
            QuerySet[Task]: QuerySet composed by tasks being processed by a developer
        """
        tasks_filtered = self.tasks.filter(assigned_to=developer.id, status = 'processing')
        return tasks_filtered

    