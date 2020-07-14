from django import forms
from employee_crud.models import *

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fullname', 'mobile', 'position', 'emp_code')
        labels = {
            'fullname':'Full Name',
            'emp_code':'EMP Code' ,
        }
        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'mobile': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'emp_code': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'position': forms.Select(attrs={
                'class': 'form-control', 'placeholder':'Select'
            }),
        }
    
    # def __init__(self, *args, **kwargs):
    #     super(EmployeeForm, self).__init__(*args, **kwargs)
    #     self.fields['position'].empty_label = 'Select Position'
    #     # self.fields['position'].required = False