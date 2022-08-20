from django.db import models
from .category import Category
from .supplier import Supplier

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    price = models.IntegerField(null=False)
    supplier = models.ForeignKey(Supplier, related_name='supplier', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
        app_label="api"