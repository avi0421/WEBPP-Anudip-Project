# invoice_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('invoices/', views.invoice_list, name='invoice_list'),  # Add this line
    path('invoice/<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('invoice/new/', views.create_invoice, name='create_invoice'),
    path('invoice/<int:pk>/edit/', views.update_invoice, name='update_invoice'),
    path('customer/new/', views.create_customer, name='create_customer'),
]