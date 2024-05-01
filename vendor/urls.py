from django.urls import path
from .views import *


urlpatterns = [
    path('vendors/', VendorView.as_view(), name = 'vendors'),
    path('vendors/<int:id>/', VendorDetailsView.as_view(), name='vendor_details'),
    path('vendors/<int:id>/performance', VendorPerformanceView.as_view(), name='vendor_performance'),
    path('purchase_orders/', PurchaseOrderView.as_view(), name = 'purchase_order'),
    path('purchase_orders/<int:id>/', PurchaseOrderCRUDView.as_view(), name = 'purchase_order_crud'),
    path('purchase_orders/<int:id>/acknowledge', POAknowledgeView.as_view(), name = 'purchase_order_acknowledge'),
    path('purchase_orders/<int:id>/delivered', PODevliveryView.as_view(), name = 'purchase_order_delivery'),
    path('purchase_orders/<int:id>/addrating', PORatingView.as_view(), name = 'purchase_order_rating'),
]