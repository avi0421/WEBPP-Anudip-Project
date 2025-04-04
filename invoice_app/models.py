from django.db import models
from django.urls import reverse
import uuid

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Invoice(models.Model):
    STATUS_CHOICES = (
        ('DRAFT', 'Draft'),
        ('SENT', 'Sent'),
        ('PAID', 'Paid'),
        ('OVERDUE', 'Overdue'),
    )
    
    invoice_number = models.CharField(max_length=20, unique=True, default=uuid.uuid4)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='invoices')
    date_created = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DRAFT')
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Invoice #{self.invoice_number} - {self.customer.name}"
    
    def get_total(self):
        return sum(item.get_total() for item in self.items.all())
    
    def get_absolute_url(self):
        return reverse('invoice_detail', args=[str(self.id)])

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.description} for Invoice #{self.invoice.invoice_number}"
    
    def get_total(self):
        return self.quantity * self.unit_price
