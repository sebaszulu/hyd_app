from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
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
        messages.success(self.request, "Cliente guardado correctamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al guardar. Verifica los campos e intenta nuevamente.")
        return super().form_invalid(form)


class AdviserCustomerFormView(LoginRequiredMixin, generic.FormView):
    template_name = "customers/add_adviser.html"
    form_class = AdviserCustomerForm
    success_url = reverse_lazy("add_adviser")
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Asesor guardado correctamente.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        form.save()
        messages.error(self.request, "Error al guardar. Verifica los campos e intenta nuevamente.")
        return super().form_invalid()

class LocationFormView(LoginRequiredMixin, generic.FormView):
    template_name = "customers/add_location.html"
    form_class = LocationForm
    success_url = reverse_lazy("add_location")
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Ubicación guardada correctamente.")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        form.save()
        messages.error(self.request, "Error al guardar. Verifica los campos e intenta nuevamente.")
        return super().form_invalid()


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "customers/customers_list.html"
    context_object_name = "customers"
    

    
