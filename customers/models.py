from django.db import models

'''
Clase de representa al agente comercial de Hoteles y Destinos
Sólo se podrán agregar desde la base de datos
'''
class SalesAdvisor(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='nombre')
    last_name = models.CharField(max_length=100, verbose_name='apellido')
    email = models.EmailField(unique=True, verbose_name='correo electrónico')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='teléfono')

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'


'''
Clase principal de la aplicación, la cual representa a los clientes
los cuales pueden ser freelancers o agencias, pero se decide dividirlos
en personas naturales o jurídicas
'''
class Customer(models.Model):
    class PersonType(models.TextChoices):
        NATURAL = 'NAT', 'Persona natural'
        JURIDICAL = 'JUR', 'Persona jurídica'

    class Mode(models.TextChoices):
        VIRTUAL = 'VIR', 'Solo Virtual'
        IN_PERSON = 'PRE', 'Presencial y Virtual'

    
    sales_advisor = models.ForeignKey(
        SalesAdvisor, on_delete=models.DO_NOTHING, verbose_name='Asesor Comercial HyD'
    )
    person_type = models.CharField(
        max_length=3,
        choices=PersonType.choices,
        default=PersonType.NATURAL,
        verbose_name='tipo',
    )
    identification = models.CharField(max_length=20, unique=True, verbose_name='identificación')

    #Para persona natural
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Apellidos')

    #Para persona juridica
    company_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Razón social')

    #Aplicable para ambas personas
    trade_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Nombre comercial')

    email = models.EmailField(unique=True, verbose_name='Correo electrónico')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Teléfono')
    principal_address = models.CharField(max_length=300, null=True, blank=True, verbose_name='Dirección')
    mode = models.CharField(
        max_length=3,
        choices=Mode.choices,
        default=Mode.VIRTUAL,
        verbose_name='modalidad',
    )
    rut = models.FileField(upload_to='documents/', verbose_name='RUT')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='creado el')
    status = models.BooleanField(default=True, verbose_name='estado')

    def is_natural(self):
        return self.person_type == self.PersonType.NATURAL
    
    def is_juridical(self):
        return self.person_type == self.PersonType.JURIDICAL
    
    def __str__(self):
        if self.is_natural():
            return f'({self.get_person_type_display()}) - {self.name} {self.last_name or ''}'
        return f'({self.get_person_type_display()}) - {self.company_name or 'Sin Razón social'}'
    
'''
Clase que representa a los Asesores de cada Agencia. 
Sólo se activa si el tipo de cliente es igual a Persona Natural
'''    
class AdviserCustomer(models.Model):
    name = models.CharField(max_length=100, verbose_name='nombre')
    last_name = models.CharField(max_length=100, verbose_name='apellido')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='teléfono')
    email = models.EmailField(unique=True, null=True, blank=True, verbose_name='correo electrónico')

    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name='cliente'
    )

    def __str__(self):
        return f'{self.name} {self.last_name} - {self.email}'
    
'''
Clase que representa la ubicación de las sede o lugar de operaciones de
cada Freelance o agencia
'''
class Location(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name='cliente'
    )
    city = models.CharField(max_length=100, verbose_name='ciudad')
    address = models.CharField(max_length=300, verbose_name='dirección')

    def __str__(self):
        return f'{self.city} - {self.address}'
