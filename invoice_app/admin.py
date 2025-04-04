from django.contrib import admin
from .models import Customer, Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'customer', 'date_created', 'due_date', 'status', 'get_total')
    list_filter = ('status', 'date_created', 'due_date')
    search_fields = ('invoice_number', 'customer__name')
    inlines = [InvoiceItemInline]
    
    def get_total(self, obj):
        return f"${obj.get_total()}"
    get_total.short_description = 'Total'

@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'invoice', 'quantity', 'unit_price', 'get_total')
    list_filter = ('invoice',)
    search_fields = ('description', 'invoice__invoice_number')
    
    def get_total(self, obj):
        return f"${obj.get_total()}"
    get_total.short_description = 'Total'