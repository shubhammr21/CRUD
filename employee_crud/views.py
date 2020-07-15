from django.shortcuts import render, redirect
from employee_crud.forms import EmployeeForm
from employee_crud.models import Employee
# Create your views here.

def employee_form_view(request, id=0):
    if request.method == 'POST':
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return redirect('employee-view')
    else:
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        context = {'form':form}
        return render(request, 'employee_form.html', context)

def employee_list_view(request):
    context = {'list' : Employee.objects.all()}
    return render(request, 'employee_list.html', context)

def employee_delete_view(request, id):
    employee = Employee.objects.get(pk=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee-view')
    context = {'employee' : employee}
    return render(request, 'employee_delete.html', context)
    