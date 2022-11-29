from django.contrib import admin
from api import models


@admin.register(models.ShopModel)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SupplierModel)
class SupplierAdmin(admin.ModelAdmin):
    pass
