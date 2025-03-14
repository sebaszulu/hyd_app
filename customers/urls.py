from django.urls import path
from .views import CustomerFormView, AdviserCustomerFormView, LocationFormView, CustomerListView

urlpatterns = [
    path('agregar-cliente/', CustomerFormView.as_view(), name='add_customer'),
    path('agregar-asesor/', AdviserCustomerFormView.as_view(), name='add_adviser'),
    path('agregar-ubicacion/', LocationFormView.as_view(), name='add_location'),
    path('', CustomerListView.as_view(), name='customer_list'),
]