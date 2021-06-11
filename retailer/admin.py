from django.contrib import admin

from .models import City, Client, Product, Provider


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["first_name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ["first_name"]
