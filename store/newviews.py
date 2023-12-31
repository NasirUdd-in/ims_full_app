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
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from rest_framework.pagination import PageNumberPagination
# supplier start
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def supplier_list(request):
    suppliers = Supplier.objects.all()
    paginator = PageNumberPagination()
    paginated_queryset = paginator.paginate_queryset(suppliers, request)

    serializer = SupplierSerializer(paginated_queryset, many=True)
    # serializer = SupplierSerializer(suppliers, many=True)
    return paginator.get_paginated_response(serializer.data)


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
# @permission_classes([IsAuthenticated])
def drop_list(request):
    drop = Drop.objects.all()
    serializer = DropSerializer(drop, many=True)
    return Response(serializer.data)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def filtered_drop_list(request):
    drop = Drop.objects.all().order_by('-created_date')
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
# @permission_classes([IsAuthenticated])
def product_list(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def filtered_product_list(request):
    drop = Product.objects.all().order_by('-created_date')
    serializer = ProductSerializer(drop, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_detail(request, pk):
    info = Product.objects.get(pk=pk)
    serializer = ProductSerializer(info)
    return Response(serializer.data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def product_create(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
# @permission_classes([IsAuthenticated])
def product_update(request, pk):
    info = Product.objects.get(pk=pk)
    serializer = ProductSerializer(info, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def product_delete(request, pk):
    info = Product.objects.get(pk=pk)
    info.delete()
    return Response(status=204)


# order start
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
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


# def render_to_pdf(template_src, context_dict={},  pdf_name='document.pdf'):
#     template = get_template(template_src)
#     html = template.render(context_dict)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'attachment; filename="{pdf_name}"'
#     pdf_status = pisa.CreatePDF(html, dest=response)

#     if pdf_status.err:
#         return HttpResponse('Some errors were encountered <pre>' + html + '</pre>')

#     return response

# def ResultList(request, order_id):
#     template_name = "invoice_template.html"
#     order = Order.objects.get(id=order_id)

#     return render_to_pdf(
#         template_name,
#         {
#             "order": order,
#             # "order_items": order.orderitem_set.all(),  # Assuming you have a related model called 'OrderItem'
#         },
#     )
# def ResultList(request, order_id):
#     template_name = "invoice_template.html"
#     records = Order.objects.get(id=order_id)

#     return render_to_pdf(
#         template_name,
#         {
#             "record": records,
#         },
#     )
