# Generated by Django 4.1.5 on 2023-02-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketApp', '0010_project_assigned_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectassigned',
            name='project',
        ),
        migrations.RemoveField(
            model_name='projectassigned',
            name='project_manager',
        ),
        migrations.AddField(
            model_name='team',
            name='composed_by',
            field=models.ManyToManyField(limit_choices_to={'role': 'DEV'}, related_name='developers', to='ticketApp.employee'),
        ),
        migrations.DeleteModel(
            name='EmployeeInTeam',
        ),
        migrations.DeleteModel(
            name='ProjectAssigned',
        ),
    ]