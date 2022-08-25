from django.db import models
from django.core.validators import MinValueValidator
from .category import Category
from .supplier import Supplier

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    price = models.PositiveIntegerField(null=False, validators=[MinValueValidator(1)])
    supplier = models.ForeignKey(Supplier, related_name='supplier', null=False, blank=False, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='category', null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'
        app_label="api"