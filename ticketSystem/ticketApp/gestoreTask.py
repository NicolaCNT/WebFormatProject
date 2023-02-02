from models import *


def AssignTask(task_to_assign, developer, tasksAssigned):
    assert(developer.role == 'Project Manager')
    tasksAssigned.developer = developer
    tasksAssigned.task = task_to_assign
