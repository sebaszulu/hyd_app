# Generated by Django 5.1.7 on 2025-03-09 21:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.AddField(
            model_name='customer',
            name='principal_address',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='dirección'),
        ),
        migrations.AlterField(
            model_name='advisercustomer',
            name='last_name',
            field=models.TextField(max_length=100, verbose_name='apellido'),
        ),
        migrations.AlterField(
            model_name='advisercustomer',
            name='name',
            field=models.TextField(max_length=100, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='advisercustomer',
            name='phone',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='teléfono'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='identification',
            field=models.TextField(max_length=20, unique=True, verbose_name='identificación'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_names',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='apellidos'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mode',
            field=models.TextField(choices=[('VIR', 'Virtual'), ('PRE', 'Presencial')], default='VIR', max_length=3, verbose_name='modalidad'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.TextField(max_length=100, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='person_type',
            field=models.CharField(choices=[('NAT', 'Persona natural'), ('JUR', 'Persona jurídica')], default='NAT', max_length=3, verbose_name='tipo'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='teléfono'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='sales_advisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customers.salesadvisor', verbose_name='asesor comercial'),
        ),
        migrations.AlterField(
            model_name='location',
            name='address',
            field=models.TextField(max_length=300, verbose_name='dirección'),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.TextField(max_length=100, verbose_name='ciudad'),
        ),
        migrations.AlterField(
            model_name='salesadvisor',
            name='first_name',
            field=models.TextField(max_length=100, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='salesadvisor',
            name='last_name',
            field=models.TextField(max_length=100, verbose_name='apellido'),
        ),
        migrations.AlterField(
            model_name='salesadvisor',
            name='phone',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='teléfono'),
        ),
    ]
