from django.urls import path
from class_based_crud.views import (
    ProductListView,
    ProductCreateView,
    ProductDeleteView,
    ProductUpdateView
)
urlpatterns = [
    path('', ProductListView.as_view(), name = 'product-view'),
    path('create/', ProductCreateView.as_view(), name = 'product-create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name = 'product-update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name = 'product-delete'),
]