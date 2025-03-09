from django.urls import path
from .views import CustomerFormView

urlpatterns = [
    path('agregar-cliente/', CustomerFormView.as_view(), name='add_customer'),
]