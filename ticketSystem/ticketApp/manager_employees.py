from .models import Employee
from .manager_tasks import ManagerTasks

class ManagerEmployees():
    employees = Employee.objects.all()
    tasks = ManagerTasks()

    def get_employees_by_role(self, role_to_filter):
        employee_with_role = self.employees.filter(role = role_to_filter)
        return employee_with_role
    
    def get_employee(self, pk):
        employee = self.employees.get(id=pk)
        return employee
    
    def get_developer_tasks_processing(self, employee_pk):
        developer = self.get_employee(employee_pk)
        developer_tasks_processing = self.tasks.filter_by(assigned_to=developer.id, status = 'processing')
        return developer_tasks_processing