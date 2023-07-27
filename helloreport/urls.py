from django.contrib import admin
from django.urls import path, include
from .  import views
from .  import viewsforapi

urlpatterns = [
    # path('', views.dashboard, name='dashboard'),
    path('profit-loss/', views.report_view, name='profit-loss'),
    path('balance-sheet/', views.balance_sheet, name='balance-sheet'),
    path('purchase/', views.purchase_view, name='purchase'),
    path('sales-view/', views.sales_view, name='sales_view'),
    path('products-view/', views.products_view, name='products_view'),
    path('suppliers-view/', views.suppliers_view, name='suppliers_view'),
    path('customers-view/', views.customers_view, name='customers_view'),
    path('account-view/', views.account_view, name='account_view'),
    path('balance-adjustment-view/', views.balance_adjustment_view, name='balance_adjustment_view'),
    path('balance-transfer-view/', views.balance_transfer_view, name='balance_transfer_view'),
   
   

    #serializer
    path('api/supplier/', viewsforapi.supplier_list, name='supplier_list'),
    path('api/supplier/<int:pk>/',viewsforapi.supplier_detail, name='supplier_detail'),
    path('api/supplier/create/', viewsforapi.supplier_create, name='supplier_create'),

     #serializer
    path('api/customer/', viewsforapi.customer_list, name='customer_list'),
    path('api/customer/<int:pk>/',viewsforapi.customer_detail, name='customer_detail'),
    path('api/customer/create/', viewsforapi.customer_create, name='customer_create'),

    path('api/product/', viewsforapi.product_list, name='product_list'),
    path('api/product/<int:pk>/',viewsforapi.product_detail, name='product_detail'),
    path('api/product/create/', viewsforapi.product_create, name='product_create'),

    path('api/purchase/', viewsforapi.purchase_list, name='purchase_list'),
    path('api/purchase/<int:pk>/',viewsforapi.purchase_detail, name='purchase_detail'),
    path('api/purchase/create/', viewsforapi.purchase_create, name='purchase_create'),

    path('api/sale/', viewsforapi.sale_list, name='sale_list'),
    path('api/sale/<int:pk>/',viewsforapi.sale_detail, name='sale_detail'),
    path('api/sale/create/', viewsforapi.sale_create, name='sale_create'),

    # path('api/report/profit/', viewsforapi.report_profit, name='report_profit'),
   
]
