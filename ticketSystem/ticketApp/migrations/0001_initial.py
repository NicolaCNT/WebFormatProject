# Generated by Django 4.1.5 on 2023-02-02 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_employee', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('role', models.CharField(choices=[('CEO', 'Chief Executive Officer'), ('PM', 'Project Manager'), ('DEV', 'Developer')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Processing', 'Task processing'), ('Completed', 'Task completed')], max_length=50)),
                ('deadline', models.DateField()),
                ('created_by', models.ForeignKey(limit_choices_to={'role': 'PM'}, on_delete=django.db.models.deletion.CASCADE, to='ticketApp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_team', models.CharField(max_length=100)),
                ('project_manager', models.OneToOneField(limit_choices_to={'role': 'PM'}, on_delete=django.db.models.deletion.CASCADE, to='ticketApp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='TaskAssigned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketApp.employee')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketApp.task')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectAssigned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketApp.project')),
                ('project_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketApp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeInTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer', models.ForeignKey(limit_choices_to={'role': 'DEV'}, on_delete=django.db.models.deletion.CASCADE, to='ticketApp.employee')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketApp.team')),
            ],
        ),
    ]
