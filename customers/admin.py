from django.contrib import admin
from .models import Customer, AdviserCustomer, SalesAdvisor, Location

# Configuración de SalesAdvisor en Django Admin
@admin.register(SalesAdvisor)
class SalesAdvisorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['first_name']

# Configuración de Customer en Django Admin
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'person_type', 'identification', 'name', 'last_name',
        'email', 'phone', 'principal_address', 'mode', 'rut_link',
        'created_at', 'status', 'sales_advisor_display'
    ]
    search_fields = ['identification', 'name', 'email']
    list_filter = ['person_type', 'mode', 'status']
    readonly_fields = ['created_at']

    # Mostrar el archivo RUT como un enlace en el admin
    def rut_link(self, obj):
        if obj.rut:
            return f'<a href="{obj.rut.url}" target="_blank">Ver RUT</a>'
        return "No disponible"
    rut_link.allow_tags = True
    rut_link.short_description = "RUT"

    # Mostrar nombre del SalesAdvisor en lugar de solo su ID
    def sales_advisor_display(self, obj):
        return obj.sales_advisor if obj.sales_advisor else "Sin Asesor"
    sales_advisor_display.short_description = "Asesor Comercial"

# Configuración de AdviserCustomer en Django Admin
@admin.register(AdviserCustomer)
class AdviserCustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'email', 'phone']
    search_fields = ['name', 'last_name', 'email']
    list_filter = ['name']

# Configuración de Location en Django Admin
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['customer', 'city', 'address']
    search_fields = ['city', 'address']
    list_filter = ['city']
