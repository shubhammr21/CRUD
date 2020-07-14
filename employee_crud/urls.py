from django.urls import path
from employee_crud.views import (
    employee_list_view,
    employee_form_view,
    employee_delete_view,
)
urlpatterns = [
    path('', employee_list_view, name = 'view'),
    path('form/', employee_form_view, name = 'create'),
    path('form/<int:id>', employee_form_view, name = 'update'),
    path('delete/<int:id>', employee_delete_view, name = 'delete'),
]