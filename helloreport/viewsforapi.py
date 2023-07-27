from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Supplier,Customers, Product, Purchase, Sale
from .serializers import SupplierSerializer,CustomerSerializer, ProductSerializer, PurchaseSerializer, SaleSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.sessions.models import Session
from rest_framework import generics
from rest_framework.response import Response



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


@api_view(['GET'])
def purchase_detail(request, pk):
    info = Purchase.objects.get(pk=pk)
    serializer = PurchaseSerializer(info)
    return Response(serializer.data)


@api_view(['POST'])
def purchase_create(request):
    serializer = PurchaseSerializer(data=request.data, many=True)
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

# Purchase start
# @api_view(['GET'])
# def report_profit(request):
#     sale = Product.objects.all()
#     serializer = ProductWithAvgPurchasePriceSerializer(sale, many=True)
#     return Response(serializer.data)
