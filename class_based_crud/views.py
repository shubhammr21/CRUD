from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from class_based_crud.models import Product
from class_based_crud.forms import ProductForm

# Create your views here.
class ProductListView(ListView):
    model           = Product
    template_name   = 'ProductList.html'

class ProductCreateView(CreateView):
    model           = Product
    form_class      = ProductForm
    template_name   = 'ProductCreate.html'

class ProductUpdateView(UpdateView):
    model           = Product
    form_class      = ProductForm
    template_name   = 'ProductCreate.html'

class ProductDeleteView(DeleteView):
    model           = Product
    template_name   = 'ProductDelete.html'
    success_url     = reverse_lazy('view')
