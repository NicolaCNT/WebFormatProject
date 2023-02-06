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
#   team_employee = models.ForeignKey(Team, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name_employee

#da cambiare per problema di dichiarazione, fare una tabella che accoppia employee con team dopo la loro dichiarazione
    

class Team(models.Model):
    name_team = models.CharField(max_length=100)
    project_manager = models.OneToOneField(Employee, on_delete=models.CASCADE, limit_choices_to={'role': Employee.PM})
    composed_by = models.ManyToManyField(Employee, related_name="developers", limit_choices_to={'role': Employee.DEV})

    def __str__(self):
        return self.name_team



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
    assigned_to = models.ManyToManyField(Employee, related_name="devs", limit_choices_to={'role': Employee.DEV})
   

    def __str__(self):
        return self.title


    def get_status(self):
        return self.status

    def set_status(self, status_to_set):
        self.status = status_to_set

    
class Project(models.Model):
    name = models.CharField(max_length=20)
    assigned_to = models.ManyToManyField(Employee, related_name="pm", limit_choices_to={'role': Employee.PM})

    def __str__(self):
        return self.name
    





