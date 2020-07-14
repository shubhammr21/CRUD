from django.shortcuts import render

# Create your views here.
def employee_list_view(request):

    context = {}
    return render(request, 'employee_list.html', context)

def employee_form_view(request):

    context = {}
    return render(request, 'employee_form.html', context)

def employee_delete_view(request):

    context = {}
    return render(request, 'employee_delete.html', context)

