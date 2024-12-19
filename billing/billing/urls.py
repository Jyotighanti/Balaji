"""
URL configuration for billing project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from billing_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.index,name='index'),
    path('companymaster',views.companymaster,name='companymaster'),

    path('state/', views.state, name='state'),
    path('update_state/', views.update_state, name='update_state'),
    path('delete_state/<int:state_id>/', views.delete_state, name='delete_state'),

    path('contact/', views.contact, name='contact'),
    path('update_contact/', views.update_contact, name='update_contact'),
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('get-contact-details/<int:contact_id>/', views.get_contact_details, name='get_contact_details'),
    # Fetch details for a specific contact

    path('uom',views.uom,name='uom'),
    path('update_uom/', views.update_uom, name='update_uom'),  # Update the name as necessary
    path('delete_uom/<int:uom_id>/', views.delete_uom, name='delete_uom'),

    path('item',views.item,name='item'),
    path('update_item/', views.update_item, name='update_item'),  # Update the name as necessary
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),  # Add this line
    path('get-item-details/', views.get_item_details, name='get_item_details'),
    # path('get-item-suggestions/', views.get_item_suggestions, name='get_item_suggestions'),
    # path('get-item-details/<str:name>/', views.get_item_details, name='get_item_details'),



    path('bank',views.bank,name='bank'),
    path('update_bank',views.update_bank,name='update_bank'),
    path('delete_bank/<int:bank_id>/', views.delete_bank, name='delete_bank'),

    path('expense',views.expense,name='expense'),
    path('update_expense',views.update_expense,name='update_expense'),
    path('delete_expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),

    path('income', views.income, name='income'),
    path('update_income', views.update_income, name='update_income'),

    path('generate_sales_invoice/', views.generate_sales_invoice, name='generate_sales_invoice'),
    # path('salesinvoiceprint/', views.salesinvoiceprint, name='salesinvoiceprint'),
    # path('generate_sales_invoice/', views.generate_sales_invoice, name='generate_sales_invoice'),
    # path('invoice_success/', views.invoice_success, name='invoice_success'),

    # path('sales_invoice_success/', views.sales_invoice_success, name='sales_invoice_success'),


    path('list_sales_invoice', views.list_sales_invoice, name='list_sales_invoice'),

    path('list_receipt', views.list_receipt, name='list_receipt'),

    path('add_receipt', views.add_receipt, name='add_receipt'),

    path('add_purchase_invoice', views.add_purchase_invoice, name='add_purchase_invoice'),

    path('list_purchase_invoice', views.list_purchase_invoice, name='list_purchase_invoice'),

    path('add_payment', views.add_payment, name='add_payment'),

    path('list_payment', views.list_payment, name='list_payment'),

    path('add_sales_quotation', views.add_sales_quotation, name='add_sales_quotation'),

    path('list_sales_quotation', views.list_sales_quotation, name='list_sales_quotation'),

    path('add_incoming_DC', views.add_incoming_DC, name='add_incoming_DC'),

    path('list_incoming_DC', views.list_incoming_DC, name='list_incoming_DC'),

    path('add_outgoing_DC', views.add_outgoing_DC, name='add_outgoing_DC'),

    path('list_outgoing_DC', views.list_outgoing_DC, name='list_outgoing_DC'),

    path('stock_adjustment', views.stock_adjustment, name='stock_adjustment'),

    path('contact_balance_adjustment', views.contact_balance_adjustment, name='contact_balance_adjustment'),

    path('expense_add', views.expense_add, name='expense_add'),

    path('expense_list', views.expense_list, name='expense_list'),

    path('income_add', views.income_add, name='income_add'),

    path('bank_transfer_add', views.bank_transfer_add, name='bank_transfer_add'),

    path('gstr1', views.gstr1, name='gstr1'),

    path('gstr2', views.gstr2, name='gstr2'),

    path('contact_balance', views.contact_balance, name='contact_balance'),

    path('contact_ledger', views.contact_ledger, name='contact_ledger'),

    path('stock_balance', views.stock_balance, name='stock_balance'),

    path('stock_ledger', views.stock_ledger, name='stock_ledger'),

    path('bank_balance', views.bank_balance, name='bank_balance'),

    path('bank_ledger', views.bank_ledger, name='bank_ledger'),

    path('sale_invoice', views.sale_invoice, name='sale_invoice'),











]
