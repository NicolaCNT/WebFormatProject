# Generated by Django 4.1.5 on 2023-02-04 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketApp', '0008_alter_task_assigned_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ManyToManyField(limit_choices_to={'role': 'DEV'}, related_name='devs', to='ticketApp.employee'),
        ),
    ]
