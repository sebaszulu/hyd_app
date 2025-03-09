from django.urls import reverse_lazy
from django.views import generic
from .models import Customer
from .forms import CustomerForm, AdviserCustomerForm, LocationForm

class CustomerFormView(generic.FormView):
    template_name = "customers/add_customer.html"
    form_class = CustomerForm
    success_url = reverse_lazy("add_customer")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["adviser_form"] = AdviserCustomerForm()
        context["location_form"] = LocationForm()
        return context

    def form_valid(self, form):
        customer_form = form
        adviser_form = AdviserCustomerForm(self.request.POST)
        location_form = LocationForm(self.request.POST)

        if adviser_form.is_valid() and location_form.is_valid():
            customer_form.save()
            adviser_form.save()
            location_form.save()
            return super().form_valid(form)
        
        return self.form_invalid(form)
    
