from django.db import models

# Create your models here.
class Companymaster(models.Model):
    companyname=models.CharField(max_length=250,null=True)
    printcompanyname = models.CharField(max_length=250, null=True)
    address1 = models.CharField(max_length=250, null=True)
    address2 = models.CharField(max_length=250, null=True)
    address3 = models.CharField(max_length=250, null=True)
    pincode = models.CharField(max_length=250, null=True)
    gsttype = models.CharField(max_length=250, null=True)
    salesentry = models.CharField(max_length=250, null=True)
    placesupply = models.CharField(max_length=250, null=True)
    salesterms = models.CharField(max_length=250, null=True)
    bankdetails = models.CharField(max_length=250, null=True)
    tax = models.CharField(max_length=250, null=True)
    invoice_no_prefix = models.CharField(max_length=250, null=True)
    dpi = models.CharField(max_length=250, null=True)
    roundoff = models.CharField(max_length=250, null=True)
    discount = models.CharField(max_length=250, null=True)
    showgst = models.CharField(max_length=250, null=True)
    descbill = models.CharField(max_length=250, null=True)
    saleinvoice = models.CharField(max_length=250, null=True)
    logo = models.CharField(max_length=250, null=True)
    billNo = models.CharField(max_length=250, null=True)
    GST = models.CharField(max_length=250, null=True)


class State(models.Model):
    statename=models.CharField(max_length=250,null=True)
    gstcode=models.CharField(max_length=250,null=True)
    active=models.CharField(max_length=250,null=True)

class Contact(models.Model):
    companyname=models.CharField(max_length=250,null=True)
    prefix=models.CharField(max_length=250,null=True)
    person=models.CharField(max_length=250,null=True)
    number=models.CharField(max_length=250,null=True)
    website=models.CharField(max_length=250,null=True)
    email=models.CharField(max_length=250,null=True)
    note1=models.CharField(max_length=250,null=True)
    note2=models.CharField(max_length=250,null=True)
    address=models.CharField(max_length=250,null=True)
    gsttype=models.CharField(max_length=250,null=True)
    active=models.CharField(max_length=250,null=True)

class UOM(models.Model):
    uom=models.CharField(max_length=250,null=True)
    gstuom=models.CharField(max_length=250,null=True)
    active=models.CharField(max_length=250,null=True)

class Item(models.Model):
    itemname = models.CharField(max_length=250, null=True)
    prefix = models.CharField(max_length=250, null=True)
    hsn = models.IntegerField(null=True)
    uom = models.CharField(max_length=250, null=True)
    good = models.CharField(max_length=250, null=True)
    rate = models.CharField(max_length=250, null=True)
    ratefrom = models.CharField(max_length=250, null=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    gst = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    cgst = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    sgst = models.DecimalField(max_digits=10,decimal_places=2, null=True, blank=True)
    igst = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    active = models.CharField(max_length=250, null=True)

class Bank(models.Model):
    bankname=models.CharField(max_length=250,null=True)
    accountNo = models.IntegerField(null=True)
    IFSC = models.CharField(max_length=250,null=True)
    address = models.CharField(max_length=250,null=True)
    details = models.CharField(max_length=250,null=True)
    active = models.CharField(max_length=250,null=True)

class Expense(models.Model):
    expense = models.CharField(max_length=250,null=True)
    active = models.CharField(max_length=250, null=True)

class Income(models.Model):
    income = models.CharField(max_length=250,null=True)
    active = models.CharField(max_length=250, null=True)



# You may need to create a Contact model or use an existing one if you have contacts with more specific fields like name, GST number, etc.

class Sale(models.Model):
    companygst = models.CharField(max_length=250,null=True)
    last_inv = models.CharField(max_length=250, null=True)
    payment = models.CharField(max_length=250, null=True)
    sales_po = models.CharField(max_length=250, null=True)
    sales_dc = models.CharField(max_length=250, null=True)
    invoice_no_prefix = models.CharField(max_length=250, null=True)
    bill_date = models.CharField(max_length=250, null=True)
    invoice_number = models.CharField(max_length=250, null=True)
    contact = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=250, null=True)
    companyname = models.CharField(max_length=250, null=True)
    contact_name = models.CharField(max_length=250, null=True)
    contact_gst_number = models.CharField(max_length=250, null=True)
    statename = models.CharField(max_length=250, null=True)
    mobile = models.CharField(max_length=250, null=True)
    pan_no = models.CharField(max_length=250, null=True)
    aadhar_no = models.CharField(max_length=250, null=True)
    e_way_bill_no = models.CharField(max_length=250, null=True)
    vehicle_no = models.CharField(max_length=250, null=True)
    order_ref_no = models.CharField(max_length=250, null=True)
    transporter = models.CharField(max_length=250, null=True)
    itemname = models.CharField(max_length=250, null=True)
    description = models.CharField(max_length=250, null=True)
    gst = models.CharField(max_length=250, null=True)
    qty = models.CharField(max_length=250, null=True)
    rate = models.CharField(max_length=250, null=True)
    amt = models.CharField(max_length=250, null=True)
    ti = models.CharField(max_length=250, null=True)
    b_rate = models.CharField(max_length=250, null=True)
    sgst_percent = models.CharField(max_length=250, null=True)
    cgst_percent = models.CharField(max_length=250, null=True)
    sgst_amount = models.CharField(max_length=250, null=True)
    cgst_amount = models.CharField(max_length=250, null=True)
    total_gst = models.CharField(max_length=250, null=True)
    st = models.CharField(max_length=250, null=True)
    sub_total = models.CharField(max_length=250, null=True)
    round_off_amount = models.CharField(max_length=250, null=True)
    bill_total = models.CharField(max_length=250, null=True)
    total_gst = models.CharField(max_length=250, null=True)
    delivery_address = models.CharField(max_length=250, null=True)
    salesterms = models.CharField(max_length=250, null=True)
    bankdetails = models.CharField(max_length=250, null=True)
    is_active = models.CharField(max_length=250, null=True)



