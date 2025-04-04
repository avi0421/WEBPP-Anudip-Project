from django.contrib import admin
from django.urls import path, include
from invoice_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('invoice_app.urls')),
     path('customer/new/', views.create_customer, name='create_customer'),
]