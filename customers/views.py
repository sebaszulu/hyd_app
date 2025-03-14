from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from .forms import CustomerForm, AdviserCustomerForm, LocationForm
from .models import Customer

class CustomerFormView(LoginRequiredMixin, generic.FormView):
    template_name = "customers/add_customer.html"
    form_class = CustomerForm
    success_url = reverse_lazy("add_customer")
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AdviserCustomerFormView(LoginRequiredMixin, generic.FormView):
    template_name = "customers/add_adviser.html"
    form_class = AdviserCustomerForm
    success_url = reverse_lazy("add_adviser")
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LocationFormView(LoginRequiredMixin, generic.FormView):
    template_name = "customers/add_location.html"
    form_class = LocationForm
    success_url = reverse_lazy("add_location")
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "customers/customers_list.html"
    context_object_name = "customers"
    

    
