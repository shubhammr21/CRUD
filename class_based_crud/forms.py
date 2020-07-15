from django import forms
from class_based_crud.models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = (
            'title',
            'description',
            'price',
            'summary',
            # 'featured',
        )
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
            }),
            'summary': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            # 'featured': forms.CheckboxInput(attrs={
            #     'class': 'form-check-input form-check-inline',
            # }),
        }
    
    # def __init__(self, *args, **kwargs):
    #     super(EmployeeForm, self).__init__(*args, **kwargs)
    #     self.fields['position'].empty_label = 'Select Position'
    #     # self.fields['position'].required = False