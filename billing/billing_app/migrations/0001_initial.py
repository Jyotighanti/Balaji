# Generated by Django 5.1.3 on 2024-12-18 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankname', models.CharField(max_length=250, null=True)),
                ('accountNo', models.IntegerField(null=True)),
                ('IFSC', models.CharField(max_length=250, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('details', models.CharField(max_length=250, null=True)),
                ('active', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Companymaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=250, null=True)),
                ('printcompanyname', models.CharField(max_length=250, null=True)),
                ('address1', models.CharField(max_length=250, null=True)),
                ('address2', models.CharField(max_length=250, null=True)),
                ('address3', models.CharField(max_length=250, null=True)),
                ('pincode', models.CharField(max_length=250, null=True)),
                ('gsttype', models.CharField(max_length=250, null=True)),
                ('salesentry', models.CharField(max_length=250, null=True)),
                ('placesupply', models.CharField(max_length=250, null=True)),
                ('salesterms', models.CharField(max_length=250, null=True)),
                ('bankdetails', models.CharField(max_length=250, null=True)),
                ('tax', models.CharField(max_length=250, null=True)),
                ('dpi', models.CharField(max_length=250, null=True)),
                ('roundoff', models.CharField(max_length=250, null=True)),
                ('discount', models.CharField(max_length=250, null=True)),
                ('showgst', models.CharField(max_length=250, null=True)),
                ('descbill', models.CharField(max_length=250, null=True)),
                ('saleinvoice', models.CharField(max_length=250, null=True)),
                ('logo', models.CharField(max_length=250, null=True)),
                ('billNo', models.CharField(max_length=250, null=True)),
                ('GST', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=250, null=True)),
                ('prefix', models.CharField(max_length=250, null=True)),
                ('person', models.CharField(max_length=250, null=True)),
                ('number', models.CharField(max_length=250, null=True)),
                ('website', models.CharField(max_length=250, null=True)),
                ('email', models.CharField(max_length=250, null=True)),
                ('note1', models.CharField(max_length=250, null=True)),
                ('note2', models.CharField(max_length=250, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('gsttype', models.CharField(max_length=250, null=True)),
                ('active', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense', models.CharField(max_length=250, null=True)),
                ('active', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.CharField(max_length=250, null=True)),
                ('active', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=250, null=True)),
                ('prefix', models.CharField(max_length=250, null=True)),
                ('hsn', models.IntegerField(null=True)),
                ('uom', models.CharField(max_length=250, null=True)),
                ('good', models.CharField(max_length=250, null=True)),
                ('rate', models.CharField(max_length=250, null=True)),
                ('ratefrom', models.CharField(max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('gst', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cgst', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sgst', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('igst', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('active', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companygst', models.CharField(max_length=250, null=True)),
                ('last_inv', models.CharField(max_length=250, null=True)),
                ('payment', models.CharField(max_length=250, null=True)),
                ('sales_po', models.CharField(max_length=250, null=True)),
                ('sales_dc', models.CharField(max_length=250, null=True)),
                ('invoice_no_prefix', models.CharField(max_length=250, null=True)),
                ('bill_date', models.CharField(max_length=250, null=True)),
                ('invoice_number', models.CharField(max_length=250, null=True)),
                ('contact', models.CharField(max_length=250, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('companyname', models.CharField(max_length=250, null=True)),
                ('contact_name', models.CharField(max_length=250, null=True)),
                ('contact_gst_number', models.CharField(max_length=250, null=True)),
                ('statename', models.CharField(max_length=250, null=True)),
                ('mobile', models.CharField(max_length=250, null=True)),
                ('pan_no', models.CharField(max_length=250, null=True)),
                ('aadhar_no', models.CharField(max_length=250, null=True)),
                ('e_way_bill_no', models.CharField(max_length=250, null=True)),
                ('vehicle_no', models.CharField(max_length=250, null=True)),
                ('order_ref_no', models.CharField(max_length=250, null=True)),
                ('transporter', models.CharField(max_length=250, null=True)),
                ('itemname', models.CharField(max_length=250, null=True)),
                ('description', models.CharField(max_length=250, null=True)),
                ('gst', models.CharField(max_length=250, null=True)),
                ('qty', models.CharField(max_length=250, null=True)),
                ('rate', models.CharField(max_length=250, null=True)),
                ('amt', models.CharField(max_length=250, null=True)),
                ('ti', models.CharField(max_length=250, null=True)),
                ('b_rate', models.CharField(max_length=250, null=True)),
                ('sgst_percent', models.CharField(max_length=250, null=True)),
                ('cgst_percent', models.CharField(max_length=250, null=True)),
                ('sgst_amount', models.CharField(max_length=250, null=True)),
                ('cgst_amount', models.CharField(max_length=250, null=True)),
                ('st', models.CharField(max_length=250, null=True)),
                ('sub_total', models.CharField(max_length=250, null=True)),
                ('round_off', models.CharField(max_length=250, null=True)),
                ('bill_total', models.CharField(max_length=250, null=True)),
                ('total_gst', models.CharField(max_length=250, null=True)),
                ('delivery_address', models.CharField(max_length=250, null=True)),
                ('salesterms', models.CharField(max_length=250, null=True)),
                ('bankdetails', models.CharField(max_length=250, null=True)),
                ('is_active', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statename', models.CharField(max_length=250, null=True)),
                ('gstcode', models.CharField(max_length=250, null=True)),
                ('active', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UOM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uom', models.CharField(max_length=250, null=True)),
                ('gstuom', models.CharField(max_length=250, null=True)),
                ('active', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GenerateSaleInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no_prefix', models.CharField(blank=True, max_length=50, null=True)),
                ('bill_date', models.DateField(blank=True, null=True)),
                ('invoice_number', models.CharField(blank=True, max_length=250, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=250, null=True)),
                ('contact_gst_number', models.CharField(blank=True, max_length=15, null=True)),
                ('companyname', models.CharField(blank=True, max_length=250, null=True)),
                ('statename', models.CharField(max_length=250, null=True)),
                ('mobile', models.CharField(blank=True, max_length=15, null=True)),
                ('pan_no', models.CharField(blank=True, max_length=10, null=True)),
                ('aadhar_no', models.CharField(blank=True, max_length=12, null=True)),
                ('e_way_bill_no', models.CharField(blank=True, max_length=50, null=True)),
                ('vehicle_no', models.CharField(blank=True, max_length=20, null=True)),
                ('order_ref_no', models.CharField(blank=True, max_length=50, null=True)),
                ('transporter', models.CharField(blank=True, max_length=250, null=True)),
                ('itemname', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('gst', models.CharField(blank=True, max_length=250, null=True)),
                ('qty', models.CharField(blank=True, max_length=250, null=True)),
                ('rate', models.CharField(blank=True, max_length=250, null=True)),
                ('amt', models.CharField(blank=True, max_length=250, null=True)),
                ('ti', models.BooleanField(default=True)),
                ('b_rate', models.CharField(blank=True, max_length=250, null=True)),
                ('sgst_percent', models.CharField(blank=True, max_length=250, null=True)),
                ('cgst_percent', models.CharField(blank=True, max_length=250, null=True)),
                ('sgst_amount', models.CharField(blank=True, max_length=250, null=True)),
                ('cgst_amount', models.CharField(blank=True, max_length=250, null=True)),
                ('total_gst', models.CharField(blank=True, max_length=250, null=True)),
                ('st', models.CharField(blank=True, max_length=250, null=True)),
                ('sub_total', models.CharField(blank=True, max_length=250, null=True)),
                ('round_off', models.CharField(blank=True, max_length=250, null=True)),
                ('bill_total', models.CharField(blank=True, max_length=250, null=True)),
                ('invoice_address', models.CharField(blank=True, max_length=250, null=True)),
                ('delivery_address', models.CharField(blank=True, max_length=250, null=True)),
                ('terms_and_conditions', models.CharField(blank=True, max_length=250, null=True)),
                ('bankdetails', models.CharField(blank=True, max_length=250, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing_app.contact')),
            ],
        ),
    ]
