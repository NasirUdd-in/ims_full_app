from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from .models import Supplier, Buyer, Season, Drop, Product, Order, Delivery
from .serializers import SupplierSerializer, BuyerSerializer, SeasonSerializer, DropSerializer, ProductSerializer,OrderSerializer, DeliverySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.sessions.models import Session
from rest_framework import generics
from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.models import User
from django.contrib.auth import logout


# supplier start
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def supplier_list(request):
    suppliers = Supplier.objects.all()
    serializer = SupplierSerializer(suppliers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def supplier_detail(request, pk):
    info = Supplier.objects.get(pk=pk)
    serializer = SupplierSerializer(info)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def supplier_create(request):
    serializer = SupplierSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def supplier_update(request, pk):
    info = Supplier.objects.get(pk=pk)
    serializer = SupplierSerializer(info, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def supplier_delete(request, pk):
    info = Supplier.objects.get(pk=pk)
    info.delete()
    return Response(status=204)

# buyer start
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def buyer_list(request):
    buyer = Buyer.objects.all()
    serializer = BuyerSerializer(buyer, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def buyer_detail(request, pk):
    info = Buyer.objects.get(pk=pk)
    serializer = BuyerSerializer(info)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def buyer_create(request):
    serializer = BuyerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def buyer_update(request, pk):
    inf0 = Buyer.objects.get(pk=pk)
    serializer = BuyerSerializer(info, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def buyer_delete(request, pk):
    info = Buyer.objects.get(pk=pk)
    info.delete()
    return Response(status=204)



# season start
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def season_list(request):
    seasons = Season.objects.all()
    serializer = SeasonSerializer(seasons, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def season_detail(request, pk):
    info = Season.objects.get(pk=pk)
    serializer = SeasonSerializer(info)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def season_create(request):
    serializer = SeasonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def season_update(request, pk):
    info = Season.objects.get(pk=pk)
    serializer = SeasonSerializer(info, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def season_delete(request, pk):
    info = Season.objects.get(pk=pk)
    info.delete()
    return Response(status=204)


# drop start
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def drop_list(request):
    drop = Drop.objects.all()
    serializer = DropSerializer(drop, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def drop_detail(request, pk):
    info = Drop.objects.get(pk=pk)
    serializer = SupplierSerializer(info)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def drop_create(request):
    serializer = DropSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def drop_update(request, pk):
    info = Drop.objects.get(pk=pk)
    serializer = SeasonSerializer(info, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def drop_delete(request, pk):
    info = Drop.objects.get(pk=pk)
    info.delete()
    return Response(status=204)



# drop start
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_list(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_detail(request, pk):
    info = Product.objects.get(pk=pk)
    serializer = ProductSerializer(info)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def product_update(request, pk):
    info = Product.objects.get(pk=pk)
    serializer = ProductSerializer(info, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def product_delete(request, pk):
    info = Product.objects.get(pk=pk)
    info.delete()
    return Response(status=204)


# order start
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_list(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_detail(request, pk):
    info = Order.objects.get(pk=pk)
    serializer = OrderSerializer(info)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def order_create(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def order_update(request, pk):
    info = Order.objects.get(pk=pk)
    serializer = OrderSerializer(info, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def order_delete(request, pk):
    info = Order.objects.get(pk=pk)
    info.delete()
    return Response(status=204)

# Delivery start
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def delivery_list(request):
    delivery = Delivery.objects.all()
    serializer = DeliverySerializer(delivery, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def delivery_detail(request, pk):
    info = Delivery.objects.get(pk=pk)
    serializer = DeliverySerializer(info)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delivery_create(request):
    serializer = DeliverySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def delivery_update(request, pk):
    info = Delivery.objects.get(pk=pk)
    serializer = DeliverySerializer(info, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delivery_delete(request, pk):
    info = Delivery.objects.get(pk=pk)
    info.delete()
    return Response(status=204)
