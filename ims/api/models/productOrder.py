from django.db import models

from api.lib.utils import name_regex, phone_regex
from api.models.customer import Customer
from api.models.product import Product

class ProductOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, related_name='customer', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    order_discount = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.id}'

    class Meta:
        verbose_name_plural = 'ProductOrders'
        app_label="api"
