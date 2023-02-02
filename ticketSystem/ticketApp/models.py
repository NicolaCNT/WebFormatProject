from django.db import models

# Create your models here.



class Employee(models.Model):

    CEO = 'CEO'
    PM = 'PM'
    DEV = 'DEV'
    ROLE_CHOICES = [
        (CEO, 'Chief Executive Officer'),
        (PM, 'Project Manager'),
        (DEV, 'Developer'),
    ]


    name_employee = models.CharField(max_length=100)
    phone_number = models.TextField()
    role = models.CharField(choices=ROLE_CHOICES, max_length=30)
#   team_employee = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_employee


#da cambiare per problema di dichiarazione, fare una tabella che accoppia employee con team dopo la loro dichiarazione


class Team(models.Model):
    name_team = models.CharField(max_length=100)
    project_manager = models.OneToOneField(Employee, on_delete=models.CASCADE, limit_choices_to={'role': Employee.PM})

    def __str__(self):
        return self.name_team


class EmployeeInTeam(models.Model):
    developer = models.ForeignKey(Employee, on_delete=models.CASCADE, limit_choices_to={'role': Employee.DEV})
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Task(models.Model):
    WAITING = 'waiting'
    PROCESSING = 'processing'
    COMPLETED = 'completed'

    STATUS_CHOICES = [
        (WAITING, 'waiting'),
        (PROCESSING, 'processing'),
        (COMPLETED, 'completed'),
    ]
    title = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default=WAITING)
    deadline = models.DateField()
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, limit_choices_to={'role': Employee.PM})

    def __str__(self):
        return self.title


    
class Project(models.Model):
    name = models.CharField(max_length=20)

class TaskAssigned(models.Model):
    developer = models.ForeignKey(Employee, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

class ProjectAssigned(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    




