from views.employee_crud import (
    employee_list_view,
    employee_form_view,
    employee_delete_view,
)
urlpatterns = [
    path('',employee_form_view, name='form')
    path('list/',employee_list_view, name='list')
    path('delete/',employee_delete_view, name='delete')
]