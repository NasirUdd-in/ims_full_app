from django.shortcuts import render,redirect
import requests
from datetime import date
from .models import Supplier
from .forms import SupplierModelForm
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
# Create your views here.

def report_view(request):
    return render(request, 'report/profit-loss.html')

def balance_sheet(request):
    return render(request, 'report/balance-sheet.html')

def purchase_view(request):
    api_url = 'http://127.0.0.1:8000/rpt/api/purchase/'

    try:
        response = requests.get(api_url)
        data = response.json()
    except requests.RequestException:
        data = []
    return render(request, 'report/purchase.html', {'data': data})

def sales_view(request):
    api_url = 'http://127.0.0.1:8000/rpt/api/sale/'

    try:
        response = requests.get(api_url)
        data = response.json()
    except requests.RequestException:
        data = []
    return render(request, 'report/sales-view.html', {'data': data})

def products_view(request):
    api_url = 'http://127.0.0.1:8000/rpt/api/product/'

    try:
        response = requests.get(api_url)
        data = response.json()
    except requests.RequestException:
        data = []
    return render(request, 'report/products.html', {'data': data})

def customers_view(request):
    api_url = 'http://127.0.0.1:8000/rpt/api/customer/'

    try:
        response = requests.get(api_url)
        data = response.json()
    except requests.RequestException:
        data = []
    return render(request, 'report/customers.html', {'data': data})

def add_customers(request):
    
    return render(request, 'report/addcustomers.html')

#suppliers

def suppliers_view(request):
    api_url = 'http://127.0.0.1:8000/rpt/api/supplier/'

    try:
        response = requests.get(api_url)
        data = response.json()
    except requests.RequestException:
        # Handle any errors here
        data = []

    return render(request, 'report/suppliers.html', {'data': data})

def update_suppliers(request, supplier_id):
    # Get the item from the database
    try:
        item = Supplier.objects.get(pk=supplier_id)
    except Supplier.DoesNotExist:
        return redirect('suppliers_view')  # Or return an error page if desired

    # Handle form submission
    if request.method == 'POST':
        form = SupplierModelForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('suppliers_view')  # Or any other page you want to redirect after the update

    # Display the form for data input
    else:
        form = SupplierModelForm(instance=item)

    return render(request, 'report/updatesupplier.html', {'form': form})

# def update_suppliers(request, id):
#     # dictionary for initial data with
#     # field names as keys
#     context ={}
 
#     # fetch the object related to passed id
#     obj = get_object_or_404( Supplier, id = id)
 
#     # pass the object as instance in form
#     form = SupplierModelForm(request.POST or None, instance = obj)
 
#     # save the data from the form and
#     # redirect to detail_view
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/"+id)
 
#     # add form dictionary to context
#     context["form"] = form
 
#     return render(request, "updatesupplier.html", context)


def add_suppliers(request):
    
    return render(request, 'report/addsuppliers.html')

def add_products(request):
    
    return render(request, 'report/addproducts.html')

def add_purchases(request):
    
    return render(request, 'report/addpurchases.html')
def add_sells(request):
    
    return render(request, 'report/addsells.html')


def report_view(request):
    api_url = 'http://127.0.0.1:8000/rpt/api/sale-report/'

    # Get the time_interval from the request's GET parameters
    time_interval = request.GET.get('time_interval')

    # Calculate start_date based on the selected time_interval
    if time_interval:
        try:
            days = int(time_interval)
            end_date = date.today()
            start_date = end_date - timedelta(days=days)
        except ValueError:
            # Handle any errors here
            start_date = None
            end_date = None
    else:
        start_date = None
        end_date = None

    # If start_date and end_date are provided, add them as query parameters to the API URL
    if start_date and end_date:
        api_url += f'?start_date={start_date}&end_date={end_date}'

    try:
        response = requests.get(api_url)
        data = response.json()
    except requests.RequestException:
        # Handle any errors here
        data = []

    return render(request, 'report/profit-loss.html', {'data': data})
    
    
def account_view(request):
    return render(request, 'report/accounting/account.html')

def balance_adjustment_view(request):
    return render(request, 'report/accounting/balance-adjustment.html')

def balance_transfer_view(request):
    return render(request, 'report/accounting/balance-transfers.html')