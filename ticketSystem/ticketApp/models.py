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
    phone_number = models.IntegerField()
    role = models.CharField(choices=ROLE_CHOICES, max_length=30)
#   team_employee = models.ForeignKey(Team, on_delete=models.CASCADE)

#da cambiare per problema di dichiarazione, fare una tabella che accoppia employee con team dopo la loro dichiarazione


class Team(models.Model):
    name_team = models.CharField(max_length=100)
    project_manager = models.OneToOneField(Employee, on_delete=models.CASCADE, limit_choices_to={'role': Employee.PM})


class EmployeeInTeam(models.Model):
    developer = models.ForeignKey(Employee, on_delete=models.CASCADE, limit_choices_to={'role': Employee.DEV})
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Task(models.Model):

    PROCESSING = 'Processing'
    COMPLETED = 'Completed'

    STATUS_CHOICES = [
        (PROCESSING, 'Task processing'),
        (COMPLETED, 'Task completed'),
    ]

    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    deadline = models.DateField()
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, limit_choices_to={'role': Employee.PM})


class Project(models.Model):
    name = models.CharField(max_length=20)

class TaskAssigned(models.Model):
    developer = models.ForeignKey(Employee, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

class ProjectAssigned(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    project_manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    




