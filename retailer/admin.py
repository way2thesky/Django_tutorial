from django.contrib import admin

from .models import City, Client, Product, Provider


class CityAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(City, CityAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Product, ProductAdmin)


class ProviderAdmin(admin.ModelAdmin):
    list_display = ["first_name"]


admin.site.register(Provider, ProviderAdmin)


class ClientAdmin(admin.ModelAdmin):
    list_display = ["first_name"]


admin.site.register(Client, ClientAdmin)
