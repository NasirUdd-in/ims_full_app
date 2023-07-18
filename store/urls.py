from django.urls import path

from .views import (
    create_supplier,
    create_buyer,
    create_season,
    create_drop,
    create_product,
    create_order,
    create_delivery,

    SupplierListView,
    BuyerListView,
    SeasonListView,
    DropListView,
    ProductListView,
    OrderListView,
    DeliveryListView,
)
from . import newviews

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-buyer/', create_buyer, name='create-buyer'),
    path('create-season/', create_season, name='create-season'),
    path('create-drop/', create_drop, name='create-drop'),
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),
    path('create-delivery/', create_delivery, name='create-delivery'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('buyer-list/', BuyerListView.as_view(), name='buyer-list'),
    path('season-list/', SeasonListView.as_view(), name='season-list'),
    path('drop-list/', DropListView.as_view(), name='drop-list'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),


    #serializer
    path('api/supplier/', newviews.supplier_list, name='supplier_list'),
    path('api/supplier/<int:pk>/', newviews.supplier_detail, name='supplier_detail'),
    path('api/supplier/create/', newviews.supplier_create, name='supplier_create'),
    path('api/supplier/update/<int:pk>/', newviews.supplier_update, name='supplier_update'),
    path('api/supplier/delete/<int:pk>/', newviews.supplier_delete, name='supplier_delete'),

    path('api/buyer/', newviews.buyer_list, name='buyer_list'),
    path('api/buyer/<int:pk>/', newviews.buyer_detail, name='buyer_detail'),
    path('api/buyer/create/', newviews.buyer_create, name='buyer_create'),
    path('api/buyer/update/<int:pk>/', newviews.buyer_update, name='buyer_update'),
    path('api/buyer/delete/<int:pk>/', newviews.buyer_delete, name='buyer_delete'),


    path('api/season/', newviews.season_list, name='season_list'),
    path('api/season/<int:pk>/', newviews.season_detail, name='season_detail'),
    path('api/season/create/', newviews.season_create, name='season_create'),
    path('api/season/update/<int:pk>/', newviews.season_update, name='season_update'),
    path('api/season/delete/<int:pk>/', newviews.season_delete, name='season_delete'),

    path('api/drop/', newviews.drop_list, name='drop_list'),
    path('api/drop/<int:pk>/', newviews.drop_detail, name='drop_detail'),
    path('api/drop/create/', newviews.drop_create, name='drop_create'),
    path('api/drop/update/<int:pk>/', newviews.drop_update, name='drop_update'),
    path('api/drop/delete/<int:pk>/', newviews.drop_delete, name='drop_delete'),

    path('api/product/', newviews.product_list, name='product_list'),
    path('api/product/<int:pk>/', newviews.product_detail, name='product_detail'),
    path('api/product/create/', newviews.product_create, name='product_create'),
    path('api/product/update/<int:pk>/', newviews.product_update, name='product_update'),
    path('api/product/delete/<int:pk>/', newviews.product_delete, name='product_delete'),

    path('api/order/', newviews.order_list, name='order_list'),
    path('api/order/<int:pk>/', newviews.order_detail, name='order_detail'),
    path('api/order/create/', newviews.order_create, name='order_create'),
    path('api/order/update/<int:pk>/', newviews.order_update, name='order_update'),
    path('api/order/delete/<int:pk>/', newviews.order_delete, name='order_delete'),

    path('api/delivery/', newviews.delivery_list, name='delivery_list'),
    path('api/delivery/<int:pk>/', newviews.delivery_detail, name='delivery_detail'),
    path('api/delivery/create/', newviews.delivery_create, name='delivery_create'),
    path('api/delivery/update/<int:pk>/', newviews.delivery_update, name='delivery_update'),
    path('api/delivery/delete/<int:pk>/', newviews.delivery_delete, name='delivery_delete'),

    
]