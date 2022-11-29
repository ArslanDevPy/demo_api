from django.db import models
from django.utils.translation import gettext as _


class ShopModel(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'shop'
        verbose_name = _("Shop")
        verbose_name_plural = _("Shops")


class SupplierModel(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=50)
    address = models.TextField(verbose_name=_("Address"))
    shop = models.ManyToManyField(to=ShopModel, related_name='supplier_shops')

    class Meta:
        db_table = 'supplier'
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")

    def __str__(self) -> str:
        return self.name

    def num_shop(self) -> int:
        return self.shop.count()
