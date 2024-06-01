from django.urls import path
from .views import *
urlpatterns = [
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('update_product/<str:product_id>/', UpdateProductView.as_view(), name='update_product'),
    path('remove_product/<str:product_id>/', RemoveProductView.as_view(), name='remove_product'),
    path('update_stock/<str:product_id>/', UpdateStockView.as_view(), name='update_stock'),
    path('process_sale/<str:product_id>/', ProcessSaleView.as_view(), name='process_sale'),
    path('report/', ReportView.as_view(), name='report'),
    path('low_stock_report/', LowStockReportView.as_view(), name='low_stock_report'),
]
