from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Invoice, Customer
from .forms import InvoiceForm, InvoiceItemFormSet, CustomerForm

# Dashboard
def dashboard(request):
    recent_invoices = Invoice.objects.all().order_by('-date_created')[:5]
    return render(request, 'invoice_app/dashboard.html', {'recent_invoices': recent_invoices})

# List Invoices
def invoice_list(request):
    invoices = Invoice.objects.all().order_by('-date_created')
    return render(request, 'invoice_app/invoice_list.html', {'invoices': invoices})

# Invoice Detail
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'invoice_app/invoice_detail.html', {'invoice': invoice})

# Create Invoice
def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        formset = InvoiceItemFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            invoice = form.save()
            formset.instance = invoice
            formset.save()
            messages.success(request, "Invoice created successfully.")
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
        formset = InvoiceItemFormSet()
    
    return render(request, 'invoice_app/invoice_form.html', {
        'form': form,
        'formset': formset,
    })

# Update Invoice
def update_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        formset = InvoiceItemFormSet(request.POST, instance=invoice)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, "Invoice updated successfully.")
            return redirect('invoice_detail', pk=invoice.pk)
    else:
        form = InvoiceForm(instance=invoice)
        formset = InvoiceItemFormSet(instance=invoice)
    
    return render(request, 'invoice_app/invoice_form.html', {
        'form': form,
        'formset': formset,
        'invoice': invoice
    })

# Create Customer
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer created successfully.')
            return redirect('invoice_list')
    else:
        form = CustomerForm()
    
    return render(request, 'invoice_app/customer.html', {'form': form})
