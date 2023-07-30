from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from .models import Supplier,Customers, Product, Purchase, Sale
from .serializers import SupplierSerializer,CustomerSerializer, ProductSerializer, PurchaseSerializer, SaleSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.sessions.models import Session
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Sum, F, DecimalField
from datetime import datetime
from decimal import Decimal

# supplier start
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def supplier_list(request):
    suppliers = Supplier.objects.all()
    serializer = SupplierSerializer(suppliers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def supplier_detail(request, pk):
    info = Supplier.objects.get(pk=pk)
    serializer = SupplierSerializer(info)
    return Response(serializer.data)


@api_view(['POST'])
def supplier_create(request):
    serializer = SupplierSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

def delete_item(request, item_id):
    # Get the item from the database
    try:
        item = Supplier.objects.get(pk=item_id)
    except Item.DoesNotExist:
        return redirect('suppliers_view')  # Or return an error page if desired

    # Handle the deletion (you can use any method to delete the item)
    item.delete()

    # Redirect to the item list page or any other desired page
    return redirect('suppliers_view')
    
def filtered_suppliers_view(request):
    name_filter = request.GET.get('name', '')

    # Query the database to get the filtered data based on 'name'
    filtered_suppliers = Supplier.objects.filter(name__icontains=name_filter).order_by('name')

    return render(request, 'report/suppliers.html', {'data': filtered_suppliers})

# Customer start
@api_view(['GET'])
def customer_list(request):
    customers = Customers.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def customer_detail(request, pk):
    info = Customers.objects.get(pk=pk)
    serializer = CustomerSerializer(info)
    return Response(serializer.data)


@api_view(['POST'])
def customer_create(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Product start
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def salelist(request):
#     # Annotate the queryset to get the sum of subtotals for each product
#     unique_product_subtotals = Sale.objects.values('product__name').annotate(
#         total_subtotal=Sum('subtotal')
#     )

#     # Create a list of dictionaries to store the result
#     result = []
#     for item in unique_product_subtotals:
#         product_name = item['product__name']
#         total_subtotal = item['total_subtotal']
#         result.append({'product_name': product_name, 'total_subtotal': total_subtotal})

#     return Response(result)


@api_view(['GET'])
def product_detail(request, pk):
    info = Product.objects.get(pk=pk)
    serializer = ProductSerializer(info)
    return Response(serializer.data)


@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# Purchase start
@api_view(['GET'])
def purchase_list(request):
    purchase = Purchase.objects.all()
    serializer = PurchaseSerializer(purchase, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def purchaselist(request):
#     # Annotate the queryset to get the sum of subtotals for each product
#     unique_product_subtotals = Purchase.objects.values('product__name').annotate(
#         total_subtotal=Sum('subtotal')
#     )

#     # Create a dictionary to store the result
#     result = {}
#     for item in unique_product_subtotals:
#         product_name = item['product__name']
#         total_subtotal = item['total_subtotal']
#         result[product_name] = total_subtotal

#     return Response(result)

def get_purchase_subtotals():
    # Replace this with the actual method or query that retrieves purchase data from the database
    # For example:
    purchase_data = Purchase.objects.values('product__name').annotate(total_subtotal=Sum('subtotal'))
    return {item['product__name']: item['total_subtotal'] for item in purchase_data}


@api_view(['GET'])
def purchase_detail(request, pk):
    info = Purchase.objects.get(pk=pk)
    serializer = PurchaseSerializer(info)
    return Response(serializer.data)


@api_view(['POST'])
def purchase_create(request):
    serializer = PurchaseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

# Purchase start
@api_view(['GET'])
def sale_list(request):
    sale = Sale.objects.all()
    serializer = SaleSerializer(sale, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def sale_detail(request, pk):
    info = Sale.objects.get(pk=pk)
    serializer = SaleSerializer(info)
    return Response(serializer.data)


@api_view(['POST'])
def sale_create(request):
    serializer = SaleSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


#hello
# @api_view(['GET'])
# def salelist(request):
#     # Get the start_date and end_date parameters from the query parameters (if available)
#     start_date_param = request.GET.get('start_date')
#     end_date_param = request.GET.get('end_date')

#     # Parse the date strings into datetime objects (if provided)
#     start_date = datetime.strptime(start_date_param, '%Y-%m-%d') if start_date_param else None
#     end_date = datetime.strptime(end_date_param, '%Y-%m-%d') if end_date_param else None

#     # Filter sales data based on the date range (if provided)
#     sales_query = Sale.objects
#     if start_date and end_date:
#         sales_query = sales_query.filter(quotation_date__range=[start_date, end_date])
#     elif start_date:
#         sales_query = sales_query.filter(quotation_date__gte=start_date)
#     elif end_date:
#         sales_query = sales_query.filter(quotation_date__lte=end_date)

#     # Annotate the queryset to get the sum of subtotals for each product sold
#     unique_product_subtotals = sales_query.values('product__name').annotate(
#         total_subtotal=Sum('subtotal')
#     )

#     # Create a dictionary to store the result of sell subtotals
#     sell_subtotals = {item['product__name']: Decimal(item['total_subtotal']) for item in unique_product_subtotals}

#     # Get the purchase subtotals
#     purchase_subtotals = get_purchase_subtotals()

#     # Calculate the difference between sell subtotal and purchase subtotal for each product
#     result = []
#     for product_name, sell_subtotal in sell_subtotals.items():
#         purchase_subtotal = purchase_subtotals.get(product_name, Decimal('0.0'))
#         difference = sell_subtotal - purchase_subtotal
#         result.append({
#             'product_name': product_name,
#             'sell_subtotal': sell_subtotal,
#             'purchase_subtotal': purchase_subtotal,
#             'difference': difference
#         })

#     return Response(result)

# @api_view(['GET'])
# def purchaselist(request):
#     # Get the start_date and end_date parameters from the query parameters (if available)
#     start_date_param = request.GET.get('start_date')
#     end_date_param = request.GET.get('end_date')

#     # Parse the date strings into datetime objects (if provided)
#     start_date = datetime.strptime(start_date_param, '%Y-%m-%d') if start_date_param else None
#     end_date = datetime.strptime(end_date_param, '%Y-%m-%d') if end_date_param else None

#     # Filter purchase data based on the date range (if provided)
#     purchase_query = Purchase.objects
#     if start_date and end_date:
#         purchase_query = purchase_query.filter(date__range=[start_date, end_date])
#     elif start_date:
#         purchase_query = purchase_query.filter(date__gte=start_date)
#     elif end_date:
#         purchase_query = purchase_query.filter(date__lte=end_date)

#     # Annotate the queryset to get the sum of subtotals for each product purchased
#     unique_product_subtotals = purchase_query.values('product__name').annotate(
#         total_subtotal=Sum('subtotal')
#     )

#     # Create a dictionary to store the result of purchase subtotals
#     result = {}
#     for item in unique_product_subtotals:
#         product_name = item['product__name']
#         total_subtotal = Decimal(item['total_subtotal'])
#         result[product_name] = total_subtotal

#     return Response(result)

# @api_view(['GET'])
# def salelist(request):
#     # Get the start_date and end_date parameters from the query parameters (if available)
#     start_date_param = request.GET.get('start_date')
#     end_date_param = request.GET.get('end_date')

#     # Parse the date strings into datetime objects (if provided)
#     start_date = datetime.strptime(start_date_param, '%Y-%m-%d') if start_date_param else None
#     end_date = datetime.strptime(end_date_param, '%Y-%m-%d') if end_date_param else None

#     # Filter sales data based on the date range (if provided)
#     sales_query = Sale.objects
#     if start_date and end_date:
#         sales_query = sales_query.filter(quotation_date__range=[start_date, end_date])
#     elif start_date:
#         sales_query = sales_query.filter(quotation_date__gte=start_date)
#     elif end_date:
#         sales_query = sales_query.filter(quotation_date__lte=end_date)

#     # Annotate the queryset to get the sum of subtotals for each product sold
#     unique_product_subtotals = sales_query.values('product__name').annotate(
#         total_subtotal=Sum('subtotal'),
        
#     )

#     # Create a dictionary to store the result of sell subtotals
#     sell_subtotals = {item['product__name']: Decimal(item['total_subtotal']) for item in unique_product_subtotals}

#     # Calculate the total sell subtotal by summing up all the individual subtotals
#     total_sell_subtotal = sum(sell_subtotals.values())

#     # Get the purchase subtotals
#     purchase_subtotals = get_purchase_subtotals()

#     # Calculate the total purchase subtotal by summing up all the individual subtotals
#     total_purchase_subtotal = sum(purchase_subtotals.values())

#     # Calculate the difference between total sell subtotal and total purchase subtotal
#     total_difference = total_sell_subtotal - total_purchase_subtotal

#     result = {
#         'total_sell_subtotal': total_sell_subtotal,
#         'total_purchase_subtotal': total_purchase_subtotal,
#         'total_difference': total_difference,
#         'product_details': []
#     }

#     # Calculate the difference between sell subtotal and purchase subtotal for each product
#     for product_name, sell_subtotal in sell_subtotals.items():
#         purchase_subtotal = purchase_subtotals.get(product_name, Decimal('0.0'))
#         difference = sell_subtotal - purchase_subtotal
#         result['product_details'].append({
#             'product_name': product_name,
#             'sell_subtotal': sell_subtotal,
#             'purchase_subtotal': purchase_subtotal,
#             'difference': difference
#         })

#     return Response(result)

# @api_view(['GET'])
# def salelist(request):
#     # Get the start_date and end_date parameters from the query parameters (if available)
#     start_date_param = request.GET.get('start_date')
#     end_date_param = request.GET.get('end_date')

#     # Parse the date strings into datetime objects (if provided)
#     start_date = datetime.strptime(start_date_param, '%Y-%m-%d') if start_date_param else None
#     end_date = datetime.strptime(end_date_param, '%Y-%m-%d') if end_date_param else None

#     # Filter sales data based on the date range (if provided)
#     sales_query = Sale.objects
#     if start_date and end_date:
#         sales_query = sales_query.filter(quotation_date__range=[start_date, end_date])
#     elif start_date:
#         sales_query = sales_query.filter(quotation_date__gte=start_date)
#     elif end_date:
#         sales_query = sales_query.filter(quotation_date__lte=end_date)

#     # Annotate the queryset to get the sum of subtotals and quantity for each product sold
#     unique_product_data = sales_query.values('product__name').annotate(
#         total_subtotal=Sum('subtotal'),
#         total_quantity=Sum('quantity')
#     )

#     # Create a dictionary to store the result of sell data
#     sell_data = {
#         item['product__name']: {
#             'total_subtotal': Decimal(item['total_subtotal']),
#             'total_quantity': item['total_quantity']
#         }
#         for item in unique_product_data
#     }

#     # Calculate the total sell subtotal and total sell quantity by summing up all the individual subtotals and quantities
#     total_sell_subtotal = sum(item['total_subtotal'] for item in sell_data.values())
#     total_sell_quantity = sum(item['total_quantity'] for item in sell_data.values())

#     # Get the purchase subtotals and quantities
#     purchase_data = purchaselist()

#     # Calculate the total purchase subtotal and total purchase quantity by summing up all the individual subtotals and quantities
#     total_purchase_subtotal = sum(purchase_data.values())
#     total_purchase_quantity = sum(purchase_data.values())

#     # Calculate the difference between total sell subtotal and total purchase subtotal
#     total_difference = total_sell_subtotal - total_purchase_subtotal

#     result = {
#         'total_sell_subtotal': total_sell_subtotal,
#         'total_sell_quantity': total_sell_quantity,
#         'total_purchase_subtotal': total_purchase_subtotal,
#         'total_purchase_quantity': total_purchase_quantity,
#         'total_difference': total_difference,
#         'product_details': []
#     }

#     # Calculate the difference between sell subtotal and purchase subtotal for each product and also add the average subtotal
#     for product_name, sell_details in sell_data.items():
#         purchase_subtotal = purchase_data.get(product_name, Decimal('0.0'))
#         sell_subtotal = sell_details['total_subtotal']
#         sell_quantity = sell_details['total_quantity']
#         purchase_quantity = purchase_data.get(product_name, 0)
#         difference = sell_subtotal - purchase_subtotal
#         average_subtotal = sell_subtotal / sell_quantity if sell_quantity > 0 else Decimal('0.0')

#         result['product_details'].append({
#             'product_name': product_name,
#             'sell_subtotal': sell_subtotal,
#             'sell_quantity': sell_quantity,
#             'purchase_subtotal': purchase_subtotal,
#             'purchase_quantity': purchase_quantity,
#             'difference': difference,
#             'average_subtotal': average_subtotal
#         })

#     return Response(result)
@api_view(['GET'])
def salelist(request):
    # Get the start_date and end_date parameters from the query parameters (if available)
    start_date_param = request.GET.get('start_date')
    end_date_param = request.GET.get('end_date')

    # Parse the date strings into datetime objects (if provided)
    start_date = datetime.strptime(start_date_param, '%Y-%m-%d') if start_date_param else None
    end_date = datetime.strptime(end_date_param, '%Y-%m-%d') if end_date_param else None

    # Filter sales data based on the date range (if provided)
    sales_query = Sale.objects.all()
    if start_date and end_date:
        sales_query = sales_query.filter(quotation_date__range=[start_date, end_date])
    elif start_date:
        sales_query = sales_query.filter(quotation_date__gte=start_date)
    elif end_date:
        sales_query = sales_query.filter(quotation_date__lte=end_date)

    # Annotate the queryset to get the sum of subtotals and quantity for each product sold
    unique_product_data = sales_query.values('product__name').annotate(
        total_subtotal=Sum('subtotal'),
        total_quantity=Sum('quantity')
    )

    # Create a dictionary to store the result of sell data
    sell_data = {
        item['product__name']: {
            'total_subtotal': Decimal(item['total_subtotal']),
            'total_quantity': item['total_quantity']
        }
        for item in unique_product_data
    }

    # Calculate the total sell subtotal and total sell quantity by summing up all the individual subtotals and quantities
    total_sell_subtotal = sum(item['total_subtotal'] for item in sell_data.values())
    total_sell_quantity = sum(item['total_quantity'] for item in sell_data.values())
    average_sell_subtotal = total_sell_subtotal/total_sell_quantity
    # Get the purchase subtotals and quantities
    purchase_data = Purchase.objects.values('product__name').annotate(
        total_subtotal=Sum('subtotal')
    )

    # Create a dictionary to store the result of purchase subtotals
    purchase_subtotals = {item['product__name']: Decimal(item['total_subtotal']) for item in purchase_data}

    # Calculate the total purchase subtotal and total purchase quantity by summing up all the individual subtotals and quantities
    total_purchase_subtotal = sum(purchase_subtotals.values())
    total_purchase_quantity = sum(purchase_subtotals.values())
    average_purchase_subtotal = total_purchase_subtotal/total_sell_quantity
    # Calculate the difference between total sell subtotal and total purchase subtotal
    total_difference = average_sell_subtotal - average_purchase_subtotal

    result = {
        'total_sell_subtotal': total_sell_subtotal,
        'total_sell_quantity': total_sell_quantity,
         'average_sell_subtotal': average_sell_subtotal,
        'total_purchase_subtotal': total_purchase_subtotal,
         'average_purchase_subtotal': average_purchase_subtotal,
        # 'total_purchase_quantity': total_purchase_quantity,
        'total_difference': total_difference,
        'product_details': []
    }

    # Calculate the difference between sell subtotal and purchase subtotal for each product and also add the average subtotal
    for product_name, sell_details in sell_data.items():
        purchase_subtotal = purchase_subtotals.get(product_name, Decimal('0.0'))
        sell_subtotal = sell_details['total_subtotal']
        sell_quantity = sell_details['total_quantity']
        purchase_quantity = purchase_subtotals.get(product_name, 0)
        difference = sell_subtotal - purchase_subtotal
        average_subtotal = sell_subtotal / sell_quantity if sell_quantity > 0 else Decimal('0.0')

        result['product_details'].append({
            'product_name': product_name,
            'sell_subtotal': sell_subtotal,
            'sell_quantity': sell_quantity,
            'purchase_subtotal': purchase_subtotal,
            'purchase_quantity': purchase_quantity,
            'difference': difference,
            'average_subtotal': average_subtotal
        })

    return Response(result)
@api_view(['GET'])
def purchaselist(request):
    # Get the start_date and end_date parameters from the query parameters (if available)
    start_date_param = request.GET.get('start_date')
    end_date_param = request.GET.get('end_date')

    # Parse the date strings into datetime objects (if provided)
    start_date = datetime.strptime(start_date_param, '%Y-%m-%d') if start_date_param else None
    end_date = datetime.strptime(end_date_param, '%Y-%m-%d') if end_date_param else None

    # Filter purchase data based on the date range (if provided)
    purchase_query = Purchase.objects
    if start_date and end_date:
        purchase_query = purchase_query.filter(date__range=[start_date, end_date])
    elif start_date:
        purchase_query = purchase_query.filter(date__gte=start_date)
    elif end_date:
        purchase_query = purchase_query.filter(date__lte=end_date)

    # Annotate the queryset to get the sum of subtotals for each product purchased
    unique_product_subtotals = purchase_query.values('product__name').annotate(
        total_subtotal=Sum('subtotal')
    )

    # Create a dictionary to store the result of purchase subtotals
    purchase_subtotals = {item['product__name']: Decimal(item['total_subtotal']) for item in unique_product_subtotals}

    # Calculate the total purchase subtotal by summing up all the individual subtotals
    total_purchase_subtotal = sum(purchase_subtotals.values())

    return Response(purchase_subtotals)
