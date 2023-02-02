# Generated by Django 4.1.5 on 2023-02-02 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketApp', '0002_task_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Waiting', 'Task waiting to be processed'), ('Processing', 'Task processing'), ('Completed', 'Task completed')], default='Waiting', max_length=50),
        ),
    ]