from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from billing_app.models import Companymaster, State, Contact, UOM, Item, Bank, Expense, Income,Sale
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def companymaster(request):
    # Get the first company in the database or None
    company = Companymaster.objects.first()

    # Fetch active states for the dropdown
    states = State.objects.filter(active='Active')  # Adjust as needed for your model

    success_message = None  # Initialize success_message variable

    if request.method == "POST":
        # Collect form data
        companyname = request.POST.get('companyName')
        printcompanyname = request.POST.get('printCompanyName')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        address3 = request.POST.get('address3')
        pincode = request.POST.get('pincode')
        gsttype = request.POST.get('gstRegType')
        salesentry = request.POST.get('noOfSalesEntry')
        placesupply = request.POST.get('defaultPlaceOfSupply')  # State selection
        salesterms = request.POST.get('saleTerms')
        bankdetails = request.POST.get('bankDetails')
        tax = request.POST.get('saleInclTax') == 'true'
        dpi = request.POST.get('dpi')
        roundoff = request.POST.get('roundOff')
        discount = request.POST.get('showDiscount') == 'true'
        showgst = request.POST.get('showGst') == 'true'
        descbill = request.POST.get('showDescription') == 'true'
        saleinvoice = request.POST.get('printAfterSale') == 'true'
        logo = request.POST.get('showLogo') == 'true'
        billNo = request.POST.get('autoBillNumber') == 'true'

        if company:
            # Update existing company
            company.companyname = companyname
            company.printcompanyname = printcompanyname
            company.address1 = address1
            company.address2 = address2
            company.address3 = address3
            company.pincode = pincode
            company.gsttype = gsttype
            company.salesentry = salesentry
            company.placesupply = placesupply
            company.salesterms = salesterms
            company.bankdetails = bankdetails
            company.tax = tax
            company.dpi = dpi
            company.roundoff = roundoff
            company.discount = discount
            company.showgst = showgst
            company.descbill = descbill
            company.saleinvoice = saleinvoice
            company.logo = logo
            company.billNo = billNo
            company.save()

            success_message = "GST details updated successfully!"  # Set success message for update
        else:
            # Create a new company record
            Companymaster.objects.create(
                companyname=companyname,
                printcompanyname=printcompanyname,
                address1=address1,
                address2=address2,
                address3=address3,
                pincode=pincode,
                gsttype=gsttype,
                salesentry=salesentry,
                placesupply=placesupply,
                salesterms=salesterms,
                bankdetails=bankdetails,
                tax=tax,
                dpi=dpi,
                roundoff=roundoff,
                discount=discount,
                showgst=showgst,
                descbill=descbill,
                saleinvoice=saleinvoice,
                logo=logo,
                billNo=billNo
            )

            success_message = "GST details added successfully!"  # Set success message for new creation

    return render(request, 'companymaster.html', {'company': company, 'states': states, 'success_message': success_message})


#Company Master Ended here

#states starts here
def state(request):
    query = request.GET.get('statelist', '')  # Get the search query from the input field
    states = State.objects.filter(statename__icontains=query) if query else State.objects.all()

    print("States:", states)  # Debug: print the states query result

    if request.method == "POST":
        statename = request.POST.get('statename')
        gstcode = request.POST.get('gstcode')
        active = request.POST.get('active')

        State.objects.create(
            statename=statename,
            gstcode=gstcode,
            active=active
        )
        return redirect('state')

    return render(request, 'state.html', {'state': states, 'search_query': query})



def update_state(request):
    if request.method == 'POST':
        state_id = request.POST.get('state_id')
        statename = request.POST.get('statename')
        gstcode = request.POST.get('gstcode')
        active = request.POST.get('active', None)

        # If the state already exists, update it; otherwise, create a new one
        state = get_object_or_404(State, id=state_id) if state_id else State()

        state.statename = statename
        state.gstcode = gstcode
        state.active = 'Active' if active else 'Inactive'

        state.save()
        return redirect('state')  # Redirect to the state list page after updating

    return redirect('state')  # Redirect to state list page in case of GET request (optional)

# View to delete a state
def delete_state(request, state_id):
    state = get_object_or_404(State, id=state_id)  # Get the state or return 404
    state.delete()  # Delete the state
    return redirect('state')  # Redirect to the state list

#State ends here

#Masters Company Contact starts Here
def contact(request):
    # Get the search query from the input field
    query = request.GET.get('search', '')
    # Filter contacts based on the search query if provided
    contact = Contact.objects.filter(
        companyname__icontains=query
    ) | Contact.objects.filter(
        person__icontains=query
    ) if query else Contact.objects.all()

    if request.method == "POST":
        companyname = request.POST.get('companyname')
        prefix = request.POST.get('prefix')
        person = request.POST.get('person')
        number = request.POST.get('number')
        website = request.POST.get('website')
        email = request.POST.get('email')
        note1 = request.POST.get('note1')
        note2 = request.POST.get('note2')
        address = request.POST.get('address')
        gsttype = request.POST.get('gsttype')
        active = request.POST.get('active')

        Contact.objects.create(
            companyname=companyname,
            prefix=prefix,
            person=person,
            number=number,
            website=website,
            email=email,
            note1=note1,
            note2=note2,
            address=address,
            gsttype=gsttype,
            active=active
        )
        return redirect('contact')  # Refresh the Contact list page after adding

    return render(request, 'contact.html', {'contact': contact, 'search_query': query})

def get_contact_details(request, contact_id):
    try:
        contact = Contact.objects.get(id=contact_id)
        # Return the required fields in JSON format
        return JsonResponse({
            'status': 'success',
            'data': {
                'contact_name': contact.person,
                'mobile': contact.number,
                'gst_number': contact.gsttype
            }
        })
    except Contact.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Contact not found'})

def update_contact(request):
    if request.method == 'POST':
        contact_id = request.POST.get('contact_id')
        # Retrieve the contact object to be updated
        contact = Contact.objects.get(id=contact_id)

        # Update the contact fields
        contact.companyname = request.POST.get('companyname')
        contact.prefix = request.POST.get('prefix')
        contact.person = request.POST.get('person')
        contact.number = request.POST.get('number')
        contact.website = request.POST.get('website')
        contact.email = request.POST.get('email')
        contact.note1 = request.POST.get('note1')
        contact.note2 = request.POST.get('note2')
        contact.address = request.POST.get('address')
        contact.gsttype = request.POST.get('gsttype')

        # Handle the "active" checkbox, set "Active" or "Inactive"
        contact.active = 'Active' if request.POST.get('active') else 'Inactive'

        # Save the updated contact
        contact.save()

        # Redirect or render a success message
        return redirect('contact')

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('contact')


#UOM starts here
def uom(request):
    query = request.GET.get('search', '')  # Get the search query from the input field
    # Filter UOMs based on the search query if provided
    uom = UOM.objects.filter(uom__icontains=query) if query else UOM.objects.all()

    if request.method == "POST":
        uom_name = request.POST.get('uom')
        gstuom = request.POST.get('gstuom')
        active = request.POST.get('active')

        UOM.objects.create(
            uom=uom_name,
            gstuom=gstuom,
            active=active
        )
        return redirect('uom')  # Refresh the UOM list page after adding

    return render(request, 'uom.html', {'uom': uom, 'search_query': query})



def update_uom(request):
    if request.method == "POST":
        uom_id = request.POST.get('uom_id')
        uom = request.POST.get('uom')
        gstuom = request.POST.get('gstuom')

        # Check if the checkbox is checked
        is_active = request.POST.get('active', 'Inactive')  # Defaults to 'Inactive' if not checked

        # Save or update the state
        data = UOM.objects.get(id=uom_id)
        data.uom = uom
        data.gstuom = gstuom
        data.active = is_active if is_active == 'Active' else 'Inactive'  # Save as 'Active' or 'Inactive'
        data.save()

        return redirect('uom')  # Replace with your redirect URL

def delete_uom(request, uom_id):
    uom = get_object_or_404(UOM, id=uom_id)
    uom.delete()
    return redirect('uom')  # Replace 'uom' with the correct name of the UOM page URL pattern
#UOM Ends here



#Item starts here
def item(request):
    query = request.GET.get('search', '')  # Get the search query from the input field
    # Filter items based on the search query if provided
    items = Item.objects.filter(
        itemname__icontains=query
    ) if query else Item.objects.all()

    uom = UOM.objects.all()

    if request.method == "POST":
        itemname = request.POST.get('itemname')
        prefix = request.POST.get('prefix')
        hsn = request.POST.get('hsn')
        uom = request.POST.get('uom')
        good = request.POST.get('good')
        rate = request.POST.get('rate')
        ratefrom = request.POST.get('ratefrom')
        description = request.POST.get('desc')
        gst = request.POST.get('gst')
        cgst = request.POST.get('cgst')
        sgst = request.POST.get('sgst')
        igst = request.POST.get('igst')
        active = request.POST.get('active')

        Item.objects.create(
            itemname=itemname,
            prefix=prefix,
            hsn=hsn,
            uom=uom,
            good=good,
            rate=rate,
            ratefrom=ratefrom,
            description=description,
            gst=gst,
            cgst=cgst,
            sgst=sgst,
            igst=igst,
            active=active
        )
        return redirect('item')
    return render(request, 'item.html', {'uom': uom, 'items': items, 'search_query': query})

def update_item(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        # Retrieve the contact object to be updated
        contact = Item.objects.get(id=item_id)

        # Update the item fields
        contact.itemname = request.POST.get('itemname')
        contact.prefix = request.POST.get('prefix')
        contact.hsn = request.POST.get('hsncode')
        contact.uom = request.POST.get('uom')
        contact.good = request.POST.get('good')
        contact.rate = request.POST.get('rate')
        contact.ratefrom = request.POST.get('ratefrom')
        contact.description = request.POST.get('description')
        contact.gst = request.POST.get('gst')
        contact.cgst = request.POST.get('cgst')
        contact.sgst = request.POST.get('sgst')
        contact.igst = request.POST.get('igst')

        # Handle the "active" checkbox, set "Active" or "Inactive"
        contact.active = 'Active' if request.POST.get('active') else 'Inactive'

        # Save the updated contact
        contact.save()

        # Redirect or render a success message
        return redirect('item')

# Delete item function

def delete_item(request, item_id):
    try:
        # Retrieve the item by ID and delete it
        item = Item.objects.get(id=item_id)
        item.delete()
    except Item.DoesNotExist:
        pass  # Handle if the item does not exist

    return redirect('item')




def get_item_details(request):
    itemname = request.GET.get('itemname', '')
    print(f"Item name received: {itemname}")  # Add this line for debugging

    if itemname:
        try:
            item = Item.objects.get(itemname=itemname)
            print(f"Item found: {item}")  # Add this line for debugging
            return JsonResponse({
                'itemname': item.itemname,
                'description': item.description,
                'gst': item.gst,
                'rate': item.rate,
            })
        except Item.DoesNotExist:
            print(f"Item not found: {itemname}")  # Add this line for debugging
            return JsonResponse({'error': 'Item not found'}, status=404)
    return JsonResponse({'error': 'No item name provided'}, status=400)

# def get_item_suggestions(request):
#     query = request.GET.get('query', '')
#     if query:
#         # Filter items by itemname containing the query (case-insensitive)
#         items = Item.objects.filter(itemname__icontains=query).values('itemname', 'description', 'gst', 'rate')
#         item_list = list(items)
#         if item_list:
#             return JsonResponse({'success': True, 'items': item_list})
#         else:
#             return JsonResponse({'success': False, 'error': 'No items found'})
#     else:
#         return JsonResponse({'success': False, 'error': 'Query parameter is required'})

# def get_item_details(request, name):
#     try:
#         item = Item.objects.get(itemname=name)
#         data = {
#             'description': item.description,
#             'gst': item.gst,
#             'rate': item.rate,
#         }
#         print("Item Details:", data)  # Debugging line
#         return JsonResponse({'success': True, 'data': data})
#     except Item.DoesNotExist:
#         return JsonResponse({'success': False, 'error': f'Item with name "{name}" not found'})
#     except Exception as e:
#         return JsonResponse({'success': False, 'error': str(e)})



#Bank starts
def bank(request):
    query = request.GET.get('search', '')  # Get the search query from the input field

    # Filter banks based on the search query if provided
    bank = Bank.objects.filter(bankname__icontains=query) if query else Bank.objects.all()  # If no search query, display all banks

    # Check if the request method is POST (form submission)
    if request.method == "POST":
        bankname = request.POST.get('bankname')
        accountNo = request.POST.get('accountNo')
        IFSC = request.POST.get('IFSC')
        address = request.POST.get('address')
        details = request.POST.get('details')
        active = request.POST.get('active')

        # Create a new bank entry
        Bank.objects.create(
            bankname=bankname,
            accountNo=accountNo,
            IFSC=IFSC,
            address=address,
            details=details,
            active=active
        )

        # Add a success message to be displayed to the user
        # messages.success(request, 'Bank added successfully!')

        # Redirect to the same page to prevent resubmission
        return redirect('bank')  # Ensure 'bank' is the correct name of the URL pattern

    return render(request, 'bank.html', {'bank': bank})

def update_bank(request):
    if request.method == 'POST':
        bank_id = request.POST.get('bank_id')
        # Retrieve the contact object to be updated
        bank = Bank.objects.get(id=bank_id)

        # Update the contact fields
        bank.bankname = request.POST.get('bankname')
        bank.accountNo = request.POST.get('accountNo')
        bank.IFSC = request.POST.get('IFSC')
        bank.address = request.POST.get('addres')
        bank.details = request.POST.get('details')

        # Handle the "active" checkbox, set "Active" or "Inactive"
        bank.active = 'Active' if request.POST.get('active') else 'Inactive'

        # Save the updated contact
        bank.save()

        # Redirect or render a success message
        return redirect('bank')

def delete_bank(request, bank_id):
    try:
        bank = Bank.objects.get(id=bank_id)
        bank.delete()
    except Bank.DoesNotExist:
        pass
    return redirect('bank')  # Redirect to the bank list page after deletion
#Bank ends here



def expense(request):
    query = request.GET.get('search', '')  # Get the search query from the input field

    # Filter expenses based on the search query if provided
    expenses = Expense.objects.filter(expense__icontains=query) if query else Expense.objects.all()  # If no search query, display all expenses

    # Check if the request method is POST (form submission)
    if request.method == "POST":
        expense_name = request.POST.get('expense')
        active = request.POST.get('active', 'Inactive')  # Default to 'Inactive'

        # Create a new expense entry
        Expense.objects.create(
            expense=expense_name,
            active=active
        )
        # After saving, add a success message and redirect back to the expense page
        messages.success(request, 'Expense added successfully!')
        return redirect('expense')  # Redirects to the expense page to display updated data

    return render(request, 'expense.html', {'expense': expenses})

# Update expense view to handle editing an existing expense
def update_expense(request):
    if request.method == "POST":
        expense_id = request.POST.get('expense_id')
        expense_name = request.POST.get('expense')
        is_active = request.POST.get('active', 'Inactive')  # Default to 'Inactive'

        # Retrieve the expense record
        try:
            expense = Expense.objects.get(id=expense_id)
            expense.expense = expense_name
            expense.active = 'Active' if is_active == 'Active' else 'Inactive'
            expense.save()
        except Expense.DoesNotExist:
            pass  # Optionally handle the error if the expense is not found

        return redirect('expense')  # Redirect to the expense list page after updating


# Delete expense view to handle deleting an expense
def delete_expense(request, expense_id):
    try:
        expense = Expense.objects.get(id=expense_id)
        expense.delete()
    except Expense.DoesNotExist:
        pass
    return redirect('expense')  # Redirect to the expense list page after deletion


#Expense ends here


#Income starts here
def income(request):
    income = Income.objects.all()  # Get the first company in the database or None
    if request.method == "POST":
        incomev = request.POST.get('income')
        active = request.POST.get('active')

        Income.objects.create(
            income=incomev,
            active=active
        )
    return render(request,'income.html',{'income': income})


def update_income(request):
    if request.method == "POST":
        income_id = request.POST.get('income_id')
        income = request.POST.get('income')

        # Check if the checkbox is checked
        is_active = request.POST.get('active', 'Inactive')  # Defaults to 'Inactive' if not checked

        # Save or update the state
        data = Income.objects.get(id=income_id)
        data.income = income
        data.active = is_active if is_active == 'Active' else 'Inactive'  # Save as 'Active' or 'Inactive'
        data.save()

        return redirect('income')  # Replace with your redirect URL

#income ends here


def generate_sales_invoice(request):
    if request.method == 'POST':
        # Extract non-item fields
        contact_id = request.POST.get('contact')
        contact = Contact.objects.get(id=contact_id) if contact_id else None

        invoice_data = {
            'companygst': request.POST.get('companygst'),
            'last_inv': request.POST.get('last_inv'),
            'payment': request.POST.get('payment'),
            'sales_po': request.POST.get('sales_po'),
            'sales_dc': request.POST.get('sales_dc'),
            'invoice_no_prefix': request.POST.get('invoice_no_prefix'),
            'bill_date': request.POST.get('bill_date'),
            'invoice_number': request.POST.get('invoice_number'),
            'contact': contact_id,
            'address': request.POST.get('address'),
            'companyname': contact.companyname if contact else '',  # Save the company name
            'contact_name': request.POST.get('contact_name'),
            'contact_gst_number': request.POST.get('contact_gst_number'),
            'statename': request.POST.get('statename'),
            'mobile': request.POST.get('mobile'),
            'pan_no': request.POST.get('pan_no'),
            'aadhar_no': request.POST.get('aadhar_no'),
            'e_way_bill_no': request.POST.get('e_way_bill_no'),
            'vehicle_no': request.POST.get('vehicle_no'),
            'order_ref_no': request.POST.get('order_ref_no'),
            'transporter': request.POST.get('transporter'),
            'sub_total': request.POST.get('sub_total'),
            'round_off_amount': request.POST.get('round_off_amount'),
            'bill_total': request.POST.get('bill_total'),
        }

        # Process each item row
        rows = len([key for key in request.POST if key.startswith('itemname_')])
        for i in range(rows):
            itemname = request.POST.get(f'itemname_{i}')
            if itemname:  # Only process rows that have an item name
                row_data = {
                    'itemname': itemname,
                    'description': request.POST.get(f'description_{i}'),
                    'gst': request.POST.get(f'gst_{i}'),
                    'qty': request.POST.get(f'qty_{i}'),
                    'rate': request.POST.get(f'rate_{i}'),
                    'amt': request.POST.get(f'amt_{i}'),
                    'ti': request.POST.get(f'ti_{i}'),
                    'b_rate': request.POST.get(f'b_rate_{i}'),
                    'sgst_percent': request.POST.get(f'sgst_percent_{i}'),
                    'cgst_percent': request.POST.get(f'cgst_percent_{i}'),
                    'sgst_amount': request.POST.get(f'sgst_amount_{i}'),
                    'cgst_amount': request.POST.get(f'cgst_amount_{i}'),
                    'total_gst': request.POST.get(f'total_gst_{i}'),
                    'st': request.POST.get(f'st_{i}'),
                }

                # Combine row-specific data with general invoice data
                complete_data = {**invoice_data, **row_data}
                sale_invoice = Sale(**complete_data)
                sale_invoice.save()

        # Redirect or display a success message
        return HttpResponse("Sales Invoice saved successfully!")

    # Fetch active contacts, states, and company for the form rendering
    contacts = Contact.objects.filter(active='Active').order_by('companyname')
    states = State.objects.filter(active='Active').order_by('statename')
    company = Companymaster.objects.first()

    # Auto-generate the next invoice number
    last_invoice = Sale.objects.order_by('-id').first()
    if last_invoice and last_invoice.invoice_number.isdigit():
        next_invoice_number = int(last_invoice.invoice_number) + 1
    else:
        next_invoice_number = 1

    # Format the invoice number with leading zeros
    formatted_invoice_number = str(next_invoice_number).zfill(2)

    # Render the form to generate a sales invoice
    return render(request, 'generate_sales_invoice.html', {
        'contacts': contacts,
        'states': states,
        'company': company,
        'next_invoice_number': formatted_invoice_number
    })


#list_sales_invioce starts here
def list_sales_invioce(request):
    return render(request,'list_sales_invioce.html')

#list_sales_invioce ends here


def list_receipt(request):
    return render(request,'list_receipt.html')

def add_receipt(request):
    return render(request, 'add_receipt.html')

def add_purchase_invoice(request):
    return render(request,'add_purchase_invoice.html')

def list_purchase_invoice(request):
    return render(request,'list_purchase_invoice.html')

def add_payment(request):
    return render(request, 'add_payment.html')

def list_payment(request):
    return render(request,'list_payment.html')

def add_sales_quotation(request):
    return render(request,'add_sales_quotation.html')

def list_sales_quotation(request):
    return render(request,'list_sales_quotation.html')

def add_incoming_DC(request):
    return render(request,'add_incoming_DC.html')

def list_incoming_DC(request):
    return render(request,'list_incoming_DC.html')

def add_outgoing_DC(request):
    return render(request,'add_outgoing_DC.html')

def list_outgoing_DC(request):
    return render(request,'list_outgoing_DC.html')

def stock_adjustment(request):
    return render(request,'stock_adjustment.html')

def contact_balance_adjustment(request):
    return render(request, 'contact_balance_adjustment.html')

def expense_add(request):
    return render(request,'expense_add.html')

def expense_list(request):
    return render(request,'expense_list.html')

def income_add(request):
    return render(request,'income_add.html')

def bank_transfer_add(request):
    return render(request,'bank_transfer_add.html')

def gstr1(request):
    return render(request,'gstr1.html')

def gstr2(request):
    return render(request,'gstr2.html')

def contact_balance(request):
    return render(request,'contact_balance.html')

def contact_ledger(request):
    return render(request,'contact_ledger.html')

def stock_balance(request):
    return render(request,'stock_balance.html')

def stock_ledger(request):
    return render(request,'stock_ledger.html')

def bank_balance(request):
    return render(request,'bank_balance.html')

def bank_ledger(request):
    return render(request,'bank_ledger.html')

def sale_invoice(request):
    return render(request,'sale_invoice.html')