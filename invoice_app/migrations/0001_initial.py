# Generated by Django 5.2 on 2025-04-04 09:56

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(default=uuid.uuid4, max_length=20, unique=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('SENT', 'Sent'), ('PAID', 'Paid'), ('OVERDUE', 'Overdue')], default='DRAFT', max_length=10)),
                ('notes', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='invoice_app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='invoice_app.invoice')),
            ],
        ),
    ]
