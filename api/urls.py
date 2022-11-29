from django.urls import path
from api import views


urlpatterns = [
    path('supplier', views.SupplierListAPIView.as_view(), name='supplier_list'),
    path('reports/supplier/', views.ReportsOfSupplierAPIView.as_view(), name="reports_supplier")
]
