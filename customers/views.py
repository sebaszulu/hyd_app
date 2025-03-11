from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomerForm, AdviserCustomerForm, LocationForm

class CustomerFormView(generic.FormView):
    template_name = "customers/add_customer.html"
    form_class = CustomerForm
    success_url = reverse_lazy("add_customer")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AdviserCustomerFormView(generic.FormView):
    template_name = "customers/add_adviser.html"
    form_class = AdviserCustomerForm
    success_url = reverse_lazy("add_adviser")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LocationFormView(generic.FormView):
    template_name = "customers/add_location.html"
    form_class = LocationForm
    success_url = reverse_lazy("add_location")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    
