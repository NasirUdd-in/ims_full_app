from django.shortcuts import render
import requests

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
    return render(request, 'report/sales-view.html')

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


def suppliers_view(request):
    api_url = 'http://127.0.0.1:8000/rpt/api/supplier/'

    try:
        response = requests.get(api_url)
        data = response.json()
    except requests.RequestException:
        # Handle any errors here
        data = []

    return render(request, 'report/suppliers.html', {'data': data})

    
def account_view(request):
    return render(request, 'report/accounting/account.html')

def balance_adjustment_view(request):
    return render(request, 'report/accounting/balance-adjustment.html')

def balance_transfer_view(request):
    return render(request, 'report/accounting/balance-transfers.html')