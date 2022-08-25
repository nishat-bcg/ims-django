from django.db import models
from django.core.validators import RegexValidator

class Supplier(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Suppliers'
        app_label="api"
