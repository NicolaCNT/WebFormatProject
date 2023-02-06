from .models import Task
from django.db.models import Q


class ManagerTasks():
    tasks = Task.objects.all()

    def get_assignable_tasks(self):
        assignable_tasks = self.tasks.filter(Q(status = 'processing') | Q(status = 'waiting'))
        return assignable_tasks
    
    def filter_by(self, **kwargs):
        tasks_filtered = self.tasks.filter(**kwargs)
        return tasks_filtered

    def get_task(self, pk):
        task = self.tasks.get(id=pk)
        return task