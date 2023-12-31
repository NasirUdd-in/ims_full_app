from rest_framework import serializers
from .models import Supplier, Customers,Product, Purchase, Sale
from rest_framework.permissions import IsAuthenticated
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password



class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'




# class ProfitReportSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ProfitReport
#         fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source='supplier.name', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
   
   
    class Meta:
        model = Purchase
        fields = '__all__'
    
class SaleSerializer(serializers.ModelSerializer):
    customers = CustomerSerializer()
    product = ProductSerializer()

    class Meta:
        model = Sale
        fields = '__all__'

